import datetime

import recharge
import shopify_delete
from config import THEMEKIT, MYSQL_ACTIVE, MYSQL_STAGING, ACTIVE_SHOP, STAGING_SHOP, STAGING_RECHARGE_API_KEY
import shopify_gets
import shopify_posts
import mysql_db
import psql_db
import os
import re
import pathlib
from tests import compare_list


def main():
    create_local_active_products = False
    create_local_staging_products = False
    is_testing = True

    # data pulled from shopify
    if create_local_active_products:
        active_products_list = shopify_gets.get_shopify_products(ACTIVE_SHOP)
        active_metafields_list = shopify_gets.get_shopify_product_metafields(ACTIVE_SHOP, active_products_list)
        mysql_db.save_options(active_products_list, MYSQL_ACTIVE)
        mysql_db.save_products(active_products_list, MYSQL_ACTIVE)
        mysql_db.save_variants(active_products_list, MYSQL_ACTIVE)
        mysql_db.save_images(active_products_list, MYSQL_ACTIVE)
        mysql_db.save_metafields(active_metafields_list, MYSQL_ACTIVE)
        mysql_db.update_products_with_metafields(MYSQL_ACTIVE)

        # data pulled from database
        product_list = mysql_db.get_db_products()

        if is_testing:
            # For testing.
            # Creates selected products(active_product_list) that are currently in local database and
            # creates those product objects in staging.
            test_product_list = []
            active_product_ids = [36849352722, 29643505682, 9012464082]
            for product_id in active_product_ids:
                test_product = mysql_db.get_db_product(product_id)
                test_product_list.append(test_product)

            formated_products = shopify_posts.generate_formated_product(test_product_list)
            new_product_staging = shopify_posts.create_shopify_products(formated_products)
            print('staging products created')

            # For testing
            # Checks the properties of the staging products and compares it to the active products

            active_products_list = []
            for prod in active_product_ids:
                shopify_prod = shopify_gets.get_shopify_product(ACTIVE_SHOP, prod)
                active_products_list.append(shopify_prod)

            staging_products_list = []
            staging_product_ids = [5296320807073, 5296321101985, 5296321757345]
            for prod in staging_product_ids:
                shopify_product = shopify_gets.get_shopify_product(STAGING_SHOP, prod)
                staging_products_list.append(shopify_product)
            compare_list(staging_products_list, active_products_list)
        else:
            print('ARE YOU SURE YOU WANT TO CREATE ALL PRODUCTS ON STAGING? Enter \"YES\" to confirm.')
            answer = input()
            if answer == 'YES':
                shopify_delete.delete_all_staging_products()

                formated_products = shopify_posts.generate_formated_product(product_list)
                new_product_id_staging = shopify_posts.create_shopify_products(formated_products)
                print('staging products created')

    # for sports jacket table updates
    # pull all staging products and its sub objects from shopify
    if create_local_staging_products:
        staging_products_list = shopify_gets.get_shopify_products(STAGING_SHOP)
        staging_metafields_list = shopify_gets.get_shopify_product_metafields(STAGING_SHOP, staging_products_list)
        # save products and sub objects
        mysql_db.save_options(staging_products_list, MYSQL_STAGING)
        mysql_db.save_products(staging_products_list, MYSQL_STAGING)
        mysql_db.save_variants(staging_products_list, MYSQL_STAGING)
        mysql_db.save_images(staging_products_list, MYSQL_STAGING)
        mysql_db.save_metafields(staging_metafields_list, MYSQL_STAGING)
        mysql_db.update_products_with_metafields(MYSQL_STAGING)

    # gets mysql products_copy
    staging_products = mysql_db.get_products_copy(MYSQL_STAGING)
    # ALTERS THE PSQL DATABASE

    # Update the products table on ellie_testing

    if not is_testing:
        print('ARE YOU SURE YOU WANT MODIFY THE PRODUCTS TABLE ON ELLIE_TESTING? Enter \"YES\" to confirm.')
        answer = input()
        if answer == 'YES':
            psql_db.save_products(staging_products)

    # Create Alternate_products table in local db
    alternate_products = mysql_db.create_alternate_products(MYSQL_STAGING)
    mysql_db.save_alternate_products(alternate_products, MYSQL_STAGING)
    # create products table in local db (same format as psql ellie_testing.products)
    product_json_list = shopify_gets.get_shopify_products_as_json(STAGING_SHOP)
    mysql_db.save_products_copy(product_json_list, MYSQL_STAGING)

    product_tags = mysql_db.create_product_tags(alternate_products)
    mysql_db.save_product_tags(product_tags, MYSQL_STAGING)

    # Saving alternate products and product tags to psql database
    if not is_testing:
        psql_db.save_alternate_products(alternate_products)
        psql_db.save_product_tags(product_tags)

    # Create recharge rulesets for the products with metafields
    if not is_testing:
        product_id_list = recharge.get_recharge_product_ids()
        for recharge_product_id in product_id_list:
            recharge.delete_recharge_product_ruleset(recharge_product_id)

        staging_metafields_list = mysql_db.get_db_product_metafields(MYSQL_STAGING)
        for metafield in staging_metafields_list:
            print('product_title: %s product_id: %s' % (metafield.value, metafield.owner_id))
            # Call rechrage create product
            recharge.create_recharge_ruleset(metafield.owner_id)


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def get_all_themes():
    today = datetime.datetime.today()
    folder_name_date = str(today.year) + '-' + str(today.month)
    output = os.popen("theme get --list -p=%s -s=%s" % (THEMEKIT['password'], THEMEKIT['store'])).read()
    print(output)
    id_and_names = re.findall(r'\[([0-9_]+)\](.*)', output)
    new_list = []
    for item in id_and_names:
        if item[1][0] == ' ':
            new_list.append((item[0], item[1][1:]))
        else:
            new_list.append((item[0], item[1]))
    path = str(pathlib.Path(__file__).parent.absolute()) + '\\themes\\'
    root_folder_exists = os.path.exists(path)
    if not root_folder_exists:
        os.mkdir(path)
        if not os.path.exists(path + '\\' + folder_name_date):
            path = path + '\\' + folder_name_date
            os.mkdir(path)
    for item in new_list:
        os.chdir(path)
        new_folder = path + '/' + item[1]
        if ':' in item[1]:
            new_folder = item[1].replace(':', '')
            print('invalid name changed to: %s ' % new_folder)
        if '/' in item[1]:
            new_folder = item[1].replace('/', '')
            print('invalid name changed to: %s ' % new_folder)
        path_exists = os.path.exists(new_folder)
        if not path_exists:
            os.mkdir(new_folder)
            os.chdir(new_folder)
            os.system('theme get -p=%s -s=%s -t=%s' % (THEMEKIT['password'], THEMEKIT['store'], item[0]))


if __name__ == '__main__':
    main()
