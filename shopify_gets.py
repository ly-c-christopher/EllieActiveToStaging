import json
import time
import shopify

from MysqlProduct import MysqlProduct
from MysqlProductImage import MysqlProductImage
from MysqlProductMetafield import MysqlProductMetafield
from MysqlProductOption import MysqlProductOption
from MysqlProductVariant import MysqlProductVariant
from PsqlProduct import PsqlProduct


def check_calls():
    headers = shopify.ShopifyResource.connection.response.headers['HTTP_X_SHOPIFY_SHOP_API_CALL_LIMIT']
    call = int(headers[0:len(headers) - 3])
    if call > 30:
        time.sleep(5)


def get_shopify_product_metafields(shop, product_list):
    shopify.ShopifyResource.set_site(shop)
    page = shopify.Product.find(limit=250)
    valid_page = len(page) >= 1
    print(len(page))
    metafields = []
    count = 1
    while valid_page:
        for product in page:
            check_calls()
            for meta in product.metafields():
                if meta.namespace == 'ellie_order_info':
                    new_metafield = MysqlProductMetafield(meta.id)
                    new_metafield.namespace = meta.namespace
                    new_metafield.key = meta.key
                    new_metafield.value = meta.value
                    new_metafield.value_type = meta.value_type
                    new_metafield.description = meta.description
                    new_metafield.owner_id = meta.owner_id
                    new_metafield.created_at = meta.created_at
                    new_metafield.updated_at = meta.updated_at
                    new_metafield.owner_resource = meta.owner_resource
                    metafields.append(new_metafield)
                    print('meta found')
                    for prod in product_list:
                        if prod.id == new_metafield.owner_id:
                            prod.metafield_id = new_metafield.id
        valid_page = page.has_next_page()
        if valid_page:
            page = page.next_page()
    return metafields


# Get shopify products. When getting products, ProductImages, ProductVariants, and ProductMetafields are included.
def get_shopify_products(shop):
    print(shop)
    shopify.ShopifyResource.set_site(shop)
    product_list = []
    print("total product count: " + str(shopify.Product.count()))

    page = shopify.Product.find(limit=250)
    valid_page = len(page) >= 1
    while valid_page:
        for product in page:
            #print(product.id)
            new_prod = MysqlProduct(product.id)
            new_prod.title = product.title
            new_prod.vendor = product.vendor
            new_prod.product_type = product.product_type
            new_prod.created_at = product.created_at
            new_prod.template_suffix = product.template_suffix
            new_prod.published_scope = product.published_scope
            new_prod.tags = product.tags
            new_prod.handle = product.handle
            new_prod.updated_at = product.updated_at
            new_prod.body_html = product.body_html
            new_prod.published_at = product.published_at

            variants = []
            for variant in product.variants:
                #print(variant.id)
                new_variant = MysqlProductVariant(variant.id)
                new_variant.product_id = new_prod.id
                new_variant.title = variant.title
                new_variant.price = variant.price
                new_variant.sku = variant.sku
                new_variant.position = variant.position
                new_variant.inventory_policy = variant.inventory_policy
                new_variant.compare_at_price = variant.compare_at_price
                new_variant.fulfillment_service = variant.fulfillment_service
                new_variant.inventory_management = variant.inventory_management
                new_variant.option1 = variant.option1
                new_variant.option2 = variant.option2
                new_variant.option3 = variant.option3
                new_variant.created_at = variant.created_at
                new_variant.updated_at = variant.updated_at
                new_variant.taxable = variant.taxable
                new_variant.barcode = variant.barcode
                new_variant.grams = variant.grams
                new_variant.image_id = variant.image_id
                new_variant.weight = variant.weight
                new_variant.weight_unit = variant.weight_unit
                new_variant.inventory_item_id = variant.inventory_item_id
                new_variant.inventory_quantity = variant.inventory_quantity
                new_variant.old_inventory_quantity = variant.old_inventory_quantity
                # new_variant.tax_code = variant.tax_code
                new_variant.requires_shipping = variant.requires_shipping
                new_variant.admin_graphql_api_id = variant.admin_graphql_api_id
                variants.append(new_variant)
            new_prod.variants = variants

            images = []
            if len(product.images) > 0:
                for image_item in product.images:
                    # print(vars(image))
                    new_image = MysqlProductImage(image_item.id)
                    new_image.product_id = new_prod.id
                    new_image.position = image_item.position
                    new_image.alt = image_item.alt
                    new_image.width = image_item.width
                    new_image.height = image_item.height
                    new_image.src = image_item.src
                    new_image.variant_ids = image_item.variant_ids
                    new_image.admin_graphql_api_id = image_item.admin_graphql_api_id
                    images.append(new_image)

            new_prod.images = images
            if len(product.images) > 0:
                if images[0].id != product.image.id:
                    print(product.id)
                    print('images[0].id: %s' % images[0].id)
                    print('images.id:    %s' % product.image.id)
                    print('====================================================')

            # print('item.options: %s' % product.options)
            options = []
            if len(product.options) > 0:
                for option in product.options:
                    # print(vars(option))
                    new_option = MysqlProductOption(option.id)
                    new_option.product_id = product.id
                    new_option.name = option.name
                    new_option.position = option.position
                    new_option.values = option.values
                    options.append(new_option)
                new_prod.options = options
            product_list.append(new_prod)
        valid_page = page.has_next_page()
        if valid_page:
            page = page.next_page()
    print('product count: ' + str(len(product_list)))
    return product_list


def get_shopify_products_as_json(shop):
    print('shop: %s'%shop)
    shopify.ShopifyResource.set_site(shop)
    product_list = []
    page = shopify.Product.find(limit=250)
    valid_page = len(page) >= 1
    while valid_page:
        for product in page:
            json_product = product.to_dict()
            new_prod = PsqlProduct(product.id)
            new_prod.title = product.title
            new_prod.vendor = product.vendor
            new_prod.product_type = product.product_type
            new_prod.created_at = product.created_at
            new_prod.template_suffix = product.template_suffix
            new_prod.published_scope = product.published_scope
            new_prod.tags = product.tags
            new_prod.handle = product.handle
            new_prod.updated_at = product.updated_at
            new_prod.body_html = product.body_html
            new_prod.published_at = product.published_at
            new_prod.variants = json_product['variants']
            new_prod.image = json_product['image']
            new_prod.images = json_product['images']
            new_prod.options = json_product['options']
            product_list.append(new_prod)
        valid_page = page.has_next_page()
        if valid_page:
            page = page.next_page()
    return product_list


def get_shopify_product(shop, product_id):
    shopify.ShopifyResource.set_site(shop)
    product = shopify.Product.find(product_id)
    return product


def get_shopify_product_image(shop, product_id):
    shopify.ShopifyResource.set_site(shop)
    images = shopify.Image.find(product_id=product_id)
    return images


def get_graphql_test(shop):
    shop = "https://elliestaging.com/admin/api/2020-04/graphql.json"
    shopify.ShopifyResource.set_site(shop)
    client = shopify.GraphQL()
    query = '''
        {
          shop {
            name
            id
          }
        }
      '''
    result = client.execute(query)
    print (result)