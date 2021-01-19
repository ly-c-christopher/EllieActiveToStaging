import config
import shopify_gets


def compare_list(new_products_staging, active_products):
    # for prod in new_products_staging:
    #     print('new_products_staging: %s' % prod)
    #
    # for acttive in active_products:
    #     print('active_products: %s'% acttive)
    print('compare_list() executed')
    i = 0

    if len(new_products_staging) == len(active_products):

        while i < len(new_products_staging):
            active_product = shopify_gets.get_shopify_product(config.ACTIVE_SHOP, active_products[i].id)
            staging_product = shopify_gets.get_shopify_product(config.STAGING_SHOP, new_products_staging[i].id)
            print('active product:  %s  ' % vars(active_product))
            print('staging proudct: %s' % vars(staging_product))
            compare_product_attributes(active_product, staging_product)
            print('===================================PRODUCT END==================================================')
            i += 1
    else:
        print('failed list length does not match')
    print('compare_list() completed')


def compare_product_attributes(a_product, s_product):
    print('compare_product_attributes() executed')
    # if a_product. != s_product.:
    #     print('active_product. %s: ' % a_product)
    #     print('staging_product. %s: ' % s_product)
    is_equal = True
    if a_product.title != s_product.title:
        is_equal = False
        print('active_product.title:  %s' % a_product.title)
        print('staging_product.title: %s' % s_product.title)
        print('------------------------------------------------------')
    if a_product.body_html != s_product.body_html:
        is_equal = False
        print('active_product.body_html:  %s ' % a_product.body_html)
        print('staging_product.body_html: %s ' % s_product.body_html)
        print('------------------------------------------------------')
    if a_product.vendor != s_product.vendor:
        is_equal = False
        print('active_product.vendor:  %s' % a_product.vendor)
        print('staging_product.vendor: %s' % s_product.vendor)
        print('------------------------------------------------------')
    if a_product.product_type != s_product.product_type:
        is_equal = False
        print('active_product.product_type:  %s' % a_product.product_type)
        print('staging_product.product_type: %s' % s_product.product_type)
        print('------------------------------------------------------')
    if a_product.handle != s_product.handle:
        is_equal = False
        print('active_product.handle:  %s' % a_product.handle)
        print('staging_product.handle: %s' % s_product.handle)
        print('------------------------------------------------------')
    if a_product.published_at != s_product.published_at:
        is_equal = False
        print('active_product.published_at:  %s' % a_product.published_at)
        print('staging_product.published_at: %s' % s_product.published_at)
        print('------------------------------------------------------')
    if a_product.template_suffix != s_product.template_suffix:
        is_equal = False
        print('active_product.template_suffix:  %s' % a_product.template_suffix)
        print('staging_product.template_suffix: %s' % s_product.template_suffix)
        print('------------------------------------------------------')
    if a_product.published_scope != s_product.published_scope:
        is_equal = False
        print('active_product.published_scope:  %s' % a_product.published_scope)
        print('staging_product.published_scope: %s' % s_product.published_scope)
        print('------------------------------------------------------')
    if a_product.tags != s_product.tags:
        is_equal = False
        print('active_product.tags:  %s' % a_product.tags)
        print('staging_product.tags: %s' % s_product.tags)
        print('------------------------------------------------------')
    if len(a_product.variants) == len(s_product.variants):
        i = 0
        while i < len(a_product.variants):
            # is_equal =
            compare_product_variant_attribute(a_product.variants[i], a_product.id, s_product.variants[i],
                                              s_product.id)
            i += 1
    else:
        is_equal = False
        print('variant count does not match')
    print('compare_product_attributes completed')
    print('!!! PRODUCT PASSED') if is_equal else print('### PRODUCT FAILED')
    return is_equal


def compare_product_variant_attribute(a_variant, a_product_id, s_variant, s_product_id):
    print('compare_product_variant_attribute() executed')
    is_equal = True
    if a_variant.image_id is not None and s_variant.image_id is not None:
        # is_equal =
        compare_product_image_attributes(a_variant.image_id, a_product_id,
                                         s_variant.image_id, s_product_id)
    else:
        if (a_variant.image_id is None and s_variant.image_id is not None) or (
                a_variant.image_id is not None and s_variant.image_id is None):
            print('variant.image_id type not matching')
            print('a_variant.image_id: %s' % a_variant.image_id)
            print('s_variant.image_id: %s' % s_variant.image_id)
            print('------------------------------------------------------')
    if a_variant.title != s_variant.title:
        is_equal = False
        print('active_variant.title : %s' % a_variant.title)
        print('staging_variant.title: %s' % s_variant.title)
        print('------------------------------------------------------')
    if a_variant.price != s_variant.price:
        is_equal = False
        print('active_variant.price : %s' % a_variant.price)
        print('staging_variant.price: %s' % s_variant.price)
        print('------------------------------------------------------')
    if a_variant.sku != s_variant.sku:
        is_equal = False
        print('active_variant.sku : %s' % a_variant.sku)
        print('staging_variant.sku: %s' % s_variant.sku)
        print('------------------------------------------------------')
    if a_variant.position != s_variant.position:
        is_equal = False
        print('active_variant.position : %s' % a_variant.position)
        print('staging_variant.position: %s' % s_variant.position)
        print('------------------------------------------------------')
    if a_variant.inventory_policy != s_variant.inventory_policy:
        is_equal = False
        print('active_variant.inventory_policy : %s' % a_variant.inventory_policy)
        print('staging_variant.inventory_policy: %s' % s_variant.inventory_policy)
        print('------------------------------------------------------')
    if a_variant.compare_at_price != s_variant.compare_at_price:
        is_equal = False
        print('active_variant.compare_at_price : %s' % a_variant.compare_at_price)
        print('staging_variant.compare_at_price: %s' % s_variant.compare_at_price)
        print('------------------------------------------------------')
    if a_variant.fulfillment_service != s_variant.fulfillment_service:
        is_equal = False
        print('active_variant.fulfillment_service : %s' % a_variant.fulfillment_service)
        print('staging_variant.fulfillment_service: %s' % s_variant.fulfillment_service)
        print('------------------------------------------------------')
    if a_variant.inventory_management != s_variant.inventory_management:
        is_equal = False
        print('active_variant.inventory_management : %s' % a_variant.inventory_management)
        print('staging_variant.inventory_management: %s' % s_variant.inventory_management)
        print('------------------------------------------------------')
    if a_variant.option1 != s_variant.option1:
        is_equal = False
        print('active_variant.option1 : %s' % a_variant.option1)
        print('staging_variant.option1: %s' % s_variant.option1)
        print('------------------------------------------------------')
    if a_variant.option2 != s_variant.option2:
        is_equal = False
        print('active_variant.option2 : %s' % a_variant.option2)
        print('staging_variant.option2: %s' % s_variant.option2)
        print('------------------------------------------------------')
    if a_variant.option3 != s_variant.option3:
        is_equal = False
        print('active_variant.option3 : %s' % a_variant.option3)
        print('staging_variant.option3: %s' % s_variant.option3)
        print('------------------------------------------------------')
    if a_variant.taxable != s_variant.taxable:
        is_equal = False
        print('active_variant.taxable : %s' % a_variant.taxable)
        print('staging_variant.taxable: %s' % s_variant.taxable)
        print('------------------------------------------------------')
    if a_variant.barcode != s_variant.barcode:
        is_equal = False
        print('active_variant.barcode : %s' % a_variant.barcode)
        print('staging_variant.barcode: %s' % s_variant.barcode)
        print('------------------------------------------------------')
    if a_variant.grams != s_variant.grams:
        is_equal = False
        print('active_variant.grams : %s' % a_variant.grams)
        print('staging_variant.grams: %s' % s_variant.grams)
        print('------------------------------------------------------')
    if a_variant.weight != s_variant.weight:
        is_equal = False
        print('active_variant.weight : %s' % a_variant.weight)
        print('staging_variant.weight: %s' % s_variant.weight)
        print('------------------------------------------------------')
    if a_variant.weight_unit != s_variant.weight_unit:
        is_equal = False
        print('active_variant.weight_unit : %s' % a_variant.weight_unit)
        print('staging_variant.weight_unit: %s' % s_variant.weight_unit)
        print('------------------------------------------------------')
    if a_variant.requires_shipping != s_variant.requires_shipping:
        is_equal = False
        print('active_variant.requires_shipping : %s' % a_variant.requires_shipping)
        print('staging_variant.requires_shipping: %s' % s_variant.requires_shipping)
    print('compare_product_variant_attribute completed')
    print('!!! PRODUCT VARIANTS PASSED') if is_equal else print('### PRODUCT VARIANTS FAILED')
    return is_equal


def compare_product_image_attributes(a_image_id, a_product_id, s_image_id, s_product_id):
    print('compare_product_image_attributes executed')
    active_images = shopify_gets.get_shopify_product_image(config.ACTIVE_SHOP, a_product_id)
    staging_images = shopify_gets.get_shopify_product_image(config.STAGING_SHOP, s_product_id)
    is_equal = True
    if len(active_images) != len(staging_images):
        print('image count does not match. ALL FAILED.')
        print('len(active_images): %s, len(staging_images): %s' % (len(active_images), len(staging_images)))
        active_count = 1
        print('---------------------------ACTIVE----------------------')
        for active in active_images:
            print(str(active_count) + ' ACTIVE: ' + str(vars(active)))
            active_count += 1
        print('------------------------STAGING------------------------')
        staging_count = 1
        for staging in staging_images:
            print(str(staging_count) + ' STAGING: ' + str(vars(staging)))
            staging_count += 1
        print('-------------------------------------------------------')
        is_equal = False
    else:
        i = 0
        while i < len(active_images):
            if active_images[i].position != staging_images[i].position:
                is_equal = False
                print('active_image[%s].position: %s' % (i, active_images[i].position))
                print('staging_image[%s].position: %s' % (i, staging_images[i].position))
                print('------------------------------------------------------')
            if active_images[i].alt != staging_images[i].alt:
                is_equal = False
                print('active_image[%s].alt: %s' % (i, active_images[i].alt))
                print('staging_image[%s].alt: %s' % (i, staging_images[i].alt))
                print('------------------------------------------------------')
            if active_images[i].width != staging_images[i].width:
                is_equal = False
                print('active_image[%s].width: %s' % (i, active_images[i].width))
                print('staging_image[%s].width: %s' % (i, staging_images[i].width))
                print('------------------------------------------------------')
            if active_images[i].height != staging_images[i].height:
                is_equal = False
                print('active_image[%s].height: %s' % (i, active_images[i].height))
                print('staging_image[%s].height: %s' % (i, staging_images[i].height))
                print('------------------------------------------------------')
            if len(active_images[i].variant_ids) != len(staging_images[i].variant_ids):
                is_equal = False
                print('active_image[%s].variant_ids: %s' % (i, active_images[i].variant_ids))
                print('staging_image[%s].variant_ids: %s' % (i, staging_images[i].variant_ids))
                print('------------------------------------------------------')
            i += 1
    print('compare_product_image_attributes completed')
    print('!!! PRODUCT IMAGES PASSED') if is_equal else print('### PRODUCT IMAGES FAILED')
    return is_equal


def verify_image_id_with_variant(active_image_id, staging_image_id):
    print()
