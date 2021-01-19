import psycopg2
import PsqlProduct
from config import config, TABLES, ELLIE_TESTING_TABLES


def get_products():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config('ellie_testing')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        cur.execute('select * from alternate_products where product_id = \'%s\'' % 1644903628851)
        alt_prods = cur.fetchall()
        for prod in alt_prods:
            print('id: %s, product_title: %s, product_id: %s, variant_id: %s, sku: %s, product_collection: %s' %
                  (prod[0], prod[1], prod[2], prod[3], prod[4], prod[5]))

        cur.execute('select * from products;')
        database_products = []
        all_products = cur.fetchall()
        for prod in all_products:
            new_product = PsqlProduct(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6], prod[7], prod[8],
                                      prod[9], prod[10], prod[11], prod[12], prod[13], prod[14], prod[15], prod[16],
                                      prod[17], prod[18])
            database_products.append(new_product)
        for prod in database_products:
            exists = False
            if prod.metafields_global_description_tag is not None or '':
                exists = True
            if prod.metafields_global_title_tag is not None or '':
                exists = True
            if exists:
                print(prod.to_string())
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def save_products(products_list):
    conn = None
    try:
        params = config('ellie_testing')
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('TRUNCATE TABLE %s' % ELLIE_TESTING_TABLES['products'])
        for product in products_list:
            sql = 'INSERT INTO ' + TABLES['ellie_testing_products'] \
                  + ' (body_html, shopify_id, handle, images, options, product_type, published_at, image, ' \
                    'published_scope, tags, template_suffix, title, metafields_global_title_tag, ' \
                    'metafields_global_description_tag, variants, vendor, created_at, updated_at) VALUES ' \
                    '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (product.body_html, product.shopify_id, product.handle, product.images, product.options,
                      product.product_type, product.published_at, product.image, product.published_scope, product.tags,
                      product.template_suffix, product.title, product.metafields_global_title_tag,
                      product.metafields_global_description_tag, product.variants, product.vendor, product.created_at,
                      product.updated_at)
            cur.execute(sql, values)
            conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def save_alternate_products(alternate_products_list):
    conn = None
    try:
        params = config('ellie_testing')
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('TRUNCATE TABLE %s' % ELLIE_TESTING_TABLES['alt_prods'])
        for alt_prod in alternate_products_list:
            sql = 'INSERT INTO ' + ELLIE_TESTING_TABLES['alt_prods'] + ' (product_title, product_id, variant_id, ' \
                                                                       'sku, product_collection) ' \
                                                                       'VALUES (%s, %s, %s, %s, %s)'

            values = (alt_prod.product_title, alt_prod.product_id, alt_prod.variant_id, alt_prod.sku,
                      alt_prod.product_collection)
            cur.execute(sql, values)
            conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def save_product_tags(product_tags_list):
    conn = None
    try:
        params = config('ellie_testing')
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('TRUNCATE TABLE %s' % ELLIE_TESTING_TABLES['prod_tags'])
        for prod_tag in product_tags_list:
            sql = 'INSERT INTO ' + ELLIE_TESTING_TABLES['prod_tags'] + ' (product_id, tag, active_start, active_end,' \
                                                                       'theme_id) VALUES (%s, %s, %s, %s, %s)'

            values = (prod_tag.product_id, prod_tag.tag, prod_tag.active_start, prod_tag.active_end, prod_tag.theme_id)
            cur.execute(sql, values)
            conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')