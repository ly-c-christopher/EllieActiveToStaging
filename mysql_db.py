import datetime
import json

from MysqlProduct import MysqlProduct
from MysqlProductImage import MysqlProductImage
from MysqlProductMetafield import MysqlProductMetafield
from MysqlProductOption import MysqlProductOption
from MysqlProductVariant import MysqlProductVariant
from AlternateProduct import AlternateProduct
from ProductTag import ProductTag
from PsqlProduct import PsqlProduct
from config import TABLES


def get_db_products(connection_name):
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM products')
    my_results = my_cursor.fetchall()
    prod_list = []
    for product in my_results:
        new_product = MysqlProduct(product[0], product[1], product[2], product[3], product[4], product[5], product[6],
                                   product[7], product[8], product[9], product[10], product[11], product[12])
        new_product.metafield_id = product[13]
        prod_list.append(new_product)
    return prod_list


def get_db_product(product_id, connection_name):
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM products where id = %s' % product_id)
    my_results = my_cursor.fetchall()
    for product in my_results:
        new_product = MysqlProduct(product[0], product[1], product[2], product[3], product[4], product[5], product[6],
                                   product[7], product[8], product[9], product[10], product[11], product[12])
        new_product.metafield_id = product[13]
        return new_product


# Returns a list of shopify variant objects
def get_db_product_variants_with_product_id_formated(product_id, connection_name):
    # shopify.ShopifyResource.set_site(STAGING_SHOP)
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM product_variants where product_id = %s' % product_id)
    my_results = my_cursor.fetchall()
    variant_list = []
    for variant in my_results:  # 0 - 26
        new_variant = MysqlProductVariant(variant[0], variant[1], variant[2], variant[3], variant[4], variant[5],
                                          variant[6],
                                          variant[7], variant[8], variant[9], variant[10], variant[11], variant[12],
                                          variant[13], variant[14], variant[15], variant[16], variant[17], variant[18],
                                          variant[19], variant[20], variant[21], variant[22], variant[23], variant[24],
                                          variant[25], variant[26])
        variant_list.append(new_variant.format())
    return variant_list


def get_db_product_variants_with_product_id(product_id, connection_name):
    # shopify.ShopifyResource.set_site(STAGING_SHOP)
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM product_variants where product_id = %s' % product_id)
    my_results = my_cursor.fetchall()
    variant_list = []
    for variant in my_results:  # 0 - 26
        new_variant = MysqlProductVariant(variant[0], variant[1], variant[2], variant[3], variant[4], variant[5],
                                          variant[6],
                                          variant[7], variant[8], variant[9], variant[10], variant[11], variant[12],
                                          variant[13], variant[14], variant[15], variant[16], variant[17], variant[18],
                                          variant[19], variant[20], variant[21], variant[22], variant[23], variant[24],
                                          variant[25], variant[26])
        variant_list.append(new_variant)
    return variant_list


def get_db_product_variants_with_variant_id(variant_id, connection_name):
    # shopify.ShopifyResource.set_site(STAGING_SHOP)
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM product_variants where id = %s' % variant_id)
    my_results = my_cursor.fetchall()
    variant_list = []
    for variant in my_results:  # 0 - 26
        new_variant = MysqlProductVariant(variant[0], variant[1], variant[2], variant[3], variant[4], variant[5],
                                          variant[6],
                                          variant[7], variant[8], variant[9], variant[10], variant[11], variant[12],
                                          variant[13], variant[14], variant[15], variant[16], variant[17], variant[18],
                                          variant[19], variant[20], variant[21], variant[22], variant[23], variant[24],
                                          variant[25], variant[26])
        variant_list.append(new_variant)
    if len(variant_list) == 1:
        return variant_list[0]
    else:
        print('SEARCHING FOR VARIANT_ID FAILED')


def get_db_product_options_with_product_id_formated(product_id, connection_name):
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM product_options where product_id = %s' % product_id)
    my_results = my_cursor.fetchall()
    options = []
    for option in my_results:
        new_option = MysqlProductOption(option[0], option[1], option[2], option[3])
        parsed_string = option[4][1:len(option[4]) - 1]
        new_option.values = list(parsed_string.split(','))
        options.append(new_option.format())
    return options


def get_db_prodcut_metafields_with_product_id_formated(product_id, connection_name):
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM product_metafields where owner_id = %s' % product_id)
    my_results = my_cursor.fetchall()
    metafield_list = []
    for metafield in my_results:
        new_metafield = MysqlProductMetafield(metafield[0], metafield[1], metafield[2], metafield[3], metafield[4],
                                              metafield[5], metafield[6], metafield[7], metafield[8], metafield[9])
        metafield_list.append(new_metafield.format())
    return metafield_list


def get_db_product_metafields_formated(connection_name):
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM product_metafields')
    my_results = my_cursor.fetchall()
    metafield_list = []
    for metafield in my_results:
        new_metafield = MysqlProductMetafield(metafield[0], metafield[1], metafield[2], metafield[3], metafield[4],
                                              metafield[5], metafield[6], metafield[7], metafield[8], metafield[9])
        metafield_list.append(new_metafield.format())
    return metafield_list


def get_db_product_metafields(connection_name):
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM product_metafields')
    my_results = my_cursor.fetchall()
    metafield_list = []
    for metafield in my_results:
        new_metafield = MysqlProductMetafield(metafield[0], metafield[1], metafield[2], metafield[3], metafield[4],
                                              metafield[5], metafield[6], metafield[7], metafield[8], metafield[9])
        metafield_list.append(new_metafield)
    return metafield_list


def get_db_product_images_with_product_id(product_id, connection_name):
    image_list = []
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * from product_images where product_id = %s;' % product_id)
    my_results = my_cursor.fetchall()
    for image in my_results:
        new_image = MysqlProductImage(image[0], image[1], image[2], image[3], image[4], image[5], image[6], image[7],
                                      image[8])
        parsed_string = new_image.variant_ids[1:len(new_image.variant_ids) - 1]
        new_image.variant_ids = list(parsed_string.split(','))
        image_list.append(new_image)
    return image_list


def save_products(products_list, connection_name):
    print('save products starting')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % (TABLES['products']))
    count = 0
    broken_count = 0
    for product in products_list:
        try:
            my_cursor = connection_name.cursor()
            sql = 'INSERT INTO ' + TABLES['products'] + ' (id, title, vendor, product_type, created_at, handle, ' \
                                                        'updated_at, published_at, template_suffix, published_scope, ' \
                                                        'tags, body_html) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,' \
                                                        ' %s, %s, %s)'
            val = (product.id, product.title, product.vendor, product.product_type,
                   product.created_at, product.handle, product.updated_at, product.published_at,
                   product.template_suffix, product.published_scope, product.tags, product.body_html)
            my_cursor.execute(sql, val)
            connection_name.commit()
            count += 1
        except:
            broken_count += 1
            print("Something broke involving product_id: " + str(product.id) + ". Broken # " + str(broken_count))
    print('save products finished')


def save_products_copy(product_list, connection_name):
    print('save products json format')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % TABLES['local_products_copy'])
    count = 0
    broken_count = 0
    for product in product_list:
        my_cursor = connection_name.cursor()
        sql = 'INSERT INTO ' + TABLES['local_products_copy'] + ' (body_html, shopify_id, handle, images, options, ' \
                                                               'product_type, published_at, image, published_scope, ' \
                                                               'tags, template_suffix, title, variants, vendor, ' \
                                                               'created_at, updated_at) VALUES (%s, %s, %s, %s, %s, ' \
                                                               '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (
            product.body_html, product.shopify_id, product.handle, json.dumps(product.images),
            json.dumps(product.options), product.product_type, product.published_at, json.dumps(product.image),
            product.published_scope, product.tags, product.template_suffix, product.title, json.dumps(product.variants),
            product.vendor, product.created_at, product.updated_at)
        my_cursor.execute(sql, val)
        connection_name.commit()
        count += 1
    print('save_local_products_copy finished')


def get_products_copy(connection_name):
    print('getting local_products_copy')
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM %s' % TABLES['local_products_copy'])
    my_results = my_cursor.fetchall()
    product_copy_list = []
    for product in my_results:
        new_product_copy = PsqlProduct(product[2], product[1], product[3], product[4], product[5], product[6],
                                       product[7], product[8], product[9], product[10], product[11], product[12],
                                       product[13], product[14], product[15], product[16], product[17], product[18])
        # print(new_product_copy.to_string())
        product_copy_list.append(new_product_copy)
    return product_copy_list


def save_variants(products_list, connection_name):
    print('save variants starting')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % (TABLES['variants']))
    for product in products_list:
        for variant in product.variants:
            sql = 'INSERT INTO ' + TABLES['variants'] + ' (id, product_id, title, price, sku, position, ' \
                                                        'inventory_policy, compare_at_price, fulfillment_service, ' \
                                                        'inventory_management, option1, option2, option3, created_at, ' \
                                                        'updated_at, taxable, barcode, grams, image_id, weight, ' \
                                                        'weight_unit,inventory_item_id, inventory_quantity, ' \
                                                        'old_inventory_quantity, tax_code, requires_shipping, ' \
                                                        'admin_graphql_api_id) VALUES (%s, %s, %s, %s, %s, %s, %s, ' \
                                                        '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' \
                                                        '%s, %s, %s,%s, %s)'
            values = (variant.id, variant.product_id, variant.title, variant.price, variant.sku,
                      variant.position, variant.inventory_policy, variant.compare_at_price, variant.fulfillment_service,
                      variant.inventory_management, variant.option1, variant.option2, variant.option3,
                      variant.created_at, variant.updated_at, variant.taxable, variant.barcode, variant.grams,
                      variant.image_id, variant.weight, variant.weight_unit, variant.inventory_item_id,
                      variant.inventory_quantity, variant.old_inventory_quantity, variant.tax_code,
                      variant.requires_shipping, variant.admin_graphql_api_id)
            my_cursor.execute(sql, values)
            connection_name.commit()
    print('save variants finished')


def save_images(products_list, connection_name):
    print('saving product images')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % TABLES['images'])
    for product in products_list:
        if len(product.images) > 0:
            for image in product.images:
                sql = 'INSERT INTO ' + TABLES['images'] + ' (id, product_id, position, alt, width, height, src, ' \
                                                          'variant_ids, admin_graphql_api_id) VALUES (%s, %s, ' \
                                                          '%s, %s, %s, %s, %s, %s, %s)'

                values = (image.id, image.product_id, image.position, image.alt, image.width,
                          image.height, image.src, str(image.variant_ids), image.admin_graphql_api_id)

                my_cursor.execute(sql, values)

                connection_name.commit()
    print('save product images finished')


def save_options(product_list, connection_name):
    print('saving product options')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % TABLES['options'])
    for product in product_list:
        if len(product.options) > 0:
            for option in product.options:
                sql = 'INSERT INTO ' + TABLES['options'] + \
                      ' (id, product_id, name, position, my_values) VALUES (%s, %s, %s, %s, %s)'
                print(str(option.values))
                values = (option.id, option.product_id, option.name, option.position, str(option.values))
                my_cursor.execute(sql, values)
                connection_name.commit()
    print('save product options finished')


def save_metafields(metafields_list, connection_name):
    print('saving product metafields')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % (TABLES['metafields']))
    for metafield in metafields_list:
        sql = 'INSERT INTO ' + TABLES['metafields'] + ' (id, namespace, my_key, my_value, my_value_type, description, ' \
                                                      'owner_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, ' \
                                                      '%s, %s, %s, %s)'
        values = (metafield.id, metafield.namespace, metafield.key, metafield.value, metafield.value_type,
                  metafield.description, metafield.owner_id, metafield.created_at, metafield.updated_at)
        my_cursor.execute(sql, values)
        connection_name.commit()
    print('save product images finished')


def update_products_with_metafields(connection_name):
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * from %s' % TABLES['metafields'])
    metafields_list = my_cursor.fetchall()
    print(len(metafields_list))

    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * from %s' % TABLES['products'])
    products_list = my_cursor.fetchall()
    print(len(products_list))
    update_count = 0
    for metafield in metafields_list:
        for product in products_list:
            if metafield[6] == product[0]:
                sql = 'UPDATE products SET metafield_id = ' + str(metafield[0]) + ' where id = ' + str(product[0])
                my_cursor.execute(sql)
                connection_name.commit()
                update_count += 1
    print('update count: %s' % update_count)


def create_alternate_products(connection_name):
    print('executing create_alternate_products')
    my_cursor = connection_name.cursor()
    my_cursor.execute('SELECT * FROM %s' % TABLES['metafields'])
    db_metafields_list = my_cursor.fetchall()
    metafields_list = []
    for metafield in db_metafields_list:
        new_metafield = MysqlProductMetafield(metafield[0], metafield[1], metafield[2], metafield[3], metafield[4],
                                              metafield[5], metafield[6], metafield[7], metafield[8], metafield[9])
        metafields_list.append(new_metafield)
    my_cursor.execute('SELECT * FROM %s' % TABLES['products'])
    db_products_list = my_cursor.fetchall()
    products_list = []
    for product in db_products_list:
        new_product = MysqlProduct(product[0], product[1], product[2], product[3], product[4], product[5], product[6],
                                   product[7], product[8], product[9], product[10], product[11], product[12])
        new_product.metafield_id = product[13]
        products_list.append(new_product)

    alternate_products = []
    for metafield in metafields_list:
        for product in products_list:
            if product.id == metafield.owner_id:
                # variant = get_db_product_variants_with_product_id(product.id, connection_name)
                for variant in get_db_product_variants_with_product_id(product.id, connection_name):
                    new_alt_product = AlternateProduct()
                    new_alt_product.product_title = product.title
                    new_alt_product.product_id = product.id
                    new_alt_product.variant_id = variant.id
                    new_alt_product.sku = variant.sku
                    new_alt_product.product_collection = metafield.value
                    alternate_products.append(new_alt_product)
    return alternate_products


def save_alternate_products(alt_products, connection_name):
    print('saving alternate products')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % (TABLES['local_alt_prods']))
    for alt_prod in alt_products:
        sql = 'INSERT INTO ' + TABLES['local_alt_prods'] + ' (product_title, product_id, variant_id, sku, ' \
                                                           'product_collection) VALUES (%s, %s, %s, %s, %s)'
        values = (alt_prod.product_title, alt_prod.product_id, alt_prod.variant_id, alt_prod.sku,
                  alt_prod.product_collection)
        my_cursor.execute(sql, values)
        connection_name.commit()
    print('saving alternate products finished')


def create_product_tags(alternate_products):
    print('creating product tags')
    alternate_products_list = []
    for alt_product in alternate_products:
        new_alt_tag_curr = ProductTag(alt_product.product_id, 'current')
        new_alt_tag_curr.active_end = last_day_of_month(datetime.datetime.today())
        new_alt_tag_skippable = ProductTag(alt_product.product_id, 'skippable')
        new_alt_tag_skippable.active_end = last_day_of_month(datetime.datetime.today())
        new_alt_tag_switchable = ProductTag(alt_product.product_id, 'switchable')
        new_alt_tag_switchable.active_end = last_day_of_month(datetime.datetime.today())
        alternate_products_list.append(new_alt_tag_curr)
        alternate_products_list.append(new_alt_tag_skippable)
        alternate_products_list.append(new_alt_tag_switchable)
    return alternate_products_list


def save_product_tags(product_tags, connection_name):
    print('saving product tags')
    my_cursor = connection_name.cursor()
    my_cursor.execute('TRUNCATE TABLE %s' % TABLES['local_product_tags'])
    for product_tag in product_tags:
        sql = 'INSERT INTO ' + TABLES['local_product_tags'] + ' (product_id, tags, active_start, active_end, ' \
                                                              'theme_id) VALUES (%s, %s, %s, %s, %s)'
        values = (product_tag.product_id, product_tag.tag, product_tag.active_start, product_tag.active_end,
                  product_tag.theme_id)
        my_cursor.execute(sql, values)
        connection_name.commit()
    print('saving product tags finished')


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    day = next_month - datetime.timedelta(days=next_month.day)
    day = day.replace(hour=23, minute=59, second=59, microsecond=999999)
    return day
