import mysql.connector
from configparser import ConfigParser

filename = 'cred.ini'


def config(section):  # section='postgresql')
    if section == 'ellie_testing':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    elif section == 'ellie_local':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    elif section == 'ellie_staging_local':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        # print(db)
        return db
    elif section == 'ellie_active_store':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    elif section == 'ellie_staging_store':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    elif section == 'recharge_staging':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
                # print('p1: %s, p2: %s' % (param[0], param[1]))
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    elif section == 'themekit':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
                # print('p1: %s, p2: %s' % (param[0], param[1]))
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db


def config_endpoint(section):
    if section == 'ellie_active_store':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        connection = 'https://%s:%s@%s.myshopify.com/admin/api/%s' % (db['api_key'], db['password'],
                                                                      db['store'], db['version'])
        return connection
    elif section == 'ellie_staging_store':
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        connection = 'https://%s:%s@%s.myshopify.com/admin/api/%s' % (db['api_key'], db['password'],
                                                                      db['store'], db['version'])
        return connection


THEMEKIT = config('themekit')
STAGING_RECHARGE_API_KEY = config('recharge_staging')['api_key']
ACTIVE_SHOP = config_endpoint('ellie_active_store')
STAGING_SHOP = config_endpoint('ellie_staging_store')
GRAPHQL_STAGING_SHOP = config_endpoint('')
MYSQL_ACTIVE = mysql.connector.connect(**config('ellie_local'))
MYSQL_STAGING = mysql.connector.connect(**config('ellie_staging_local'))
TABLES = {'images': 'product_images',
          'products': 'products',
          'variants': 'product_variants',
          'metafields': 'product_metafields',
          'piv': 'product_image_variants',
          'options': 'product_options',
          'local_alt_prods': 'mysql_alternate_products',
          'local_products_copy': 'mysql_products',
          'local_product_tags': 'mysql_product_tags'
          }

ELLIE_TESTING_TABLES = {
    'products': 'products',
    'alt_prods': 'alternate_products',
    'prod_tags': 'product_tags'
}
