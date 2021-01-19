import shopify
import config
import mysql_db


def bubble_sort(images):
    n = len(images)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if images[j].position > images[j + 1].position:
                images[j], images[j + 1] = images[j + 1], images[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
    for image in images:
        print(image.to_string())
    return images


def create_shopify_products(product_list):
    product_id_list = []
    shopify.ShopifyResource.set_site(config.STAGING_SHOP)
    for product in product_list:
        print('db product_id: %s' % product.id)
        new_product = shopify.Product()
        new_product.title = 'test_product!: ' + product.title
        new_product.vendor = product.vendor
        new_product.product_type = product.product_type
        new_product.template_suffix = product.template_suffix
        new_product.published_scope = product.published_scope
        new_product.tags = product.tags
        new_product.handle = product.handle
        new_product.published_at = product.published_at
        new_product.body_html = product.body_html
        new_product.variants = product.variants
        new_product.options = product.options
        new_product.save()
        print()
        for var in new_product.variants:
            print('variant_id: %s, image_id: %s, sku: %s' % (var.id, var.image_id, var.sku))
        image_src_list = []

        if product.images is not None:
            product.images = bubble_sort(product.images)
            for image in product.images:
                temp_image = shopify.Image({'product_id': new_product.id})
                temp_image.src = image.src
                # temp_image.variant_ids = image.variant_ids
                db_image_variant_ids = image.variant_ids
                print(db_image_variant_ids)
                new_variant_id_list = []
                if len(db_image_variant_ids) > 0:
                    if db_image_variant_ids[0] != '':
                        for variant_id in db_image_variant_ids:
                            temp_var = mysql_db.get_db_product_variants_with_variant_id(variant_id)
                            for new_var in new_product.variants:
                                if new_var.sku == temp_var.sku:
                                    new_variant_id_list.append(new_var.id)
                temp_image.variant_ids = new_variant_id_list
                temp_image.position = image.position
                print('image.position: %s ' % image.position)
                print('image.variant_ids: %s' % image.variant_ids)
                image_src_list.append(temp_image)
                temp_image.save()
                print(vars(temp_image))
        new_product.images = image_src_list

        new_product.save()
        print('len(image_src_list): %s ' % len(image_src_list))
        print('%s images created for product_id: %s' % (len(new_product.images), new_product.id))
        print('-----------------------------------image details end-------------------------------------')

        if len(product.metafields) > 0:
            for meta in product.metafields:
                new_product.add_metafield(shopify.Metafield(meta))
        new_product.save()
        if new_product.errors:
            print('ERROR! : %s' % new_product.errors.full_messages())
        product_id_list.append(new_product)

    return product_id_list


def generate_formated_product(product_list):
    for product in product_list:
        product.metafields = mysql_db.get_db_prodcut_metafields_with_product_id_formated(product.id)
        product.variants = mysql_db.get_db_product_variants_with_product_id_formated(product.id)
        product.options = mysql_db.get_db_product_options_with_product_id_formated(product.id)

        product.images = mysql_db.get_db_product_images_with_product_id(product.id)
        if len(product.images) == 0:
            product.images = None
            product.image = None
        else:
            product.image = product.images[0]
    return product_list
