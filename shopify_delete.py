import shopify

from config import STAGING_SHOP


def delete_all_staging_products():
    shopify.ShopifyResource.set_site(STAGING_SHOP)
    page = shopify.Product.find(limit=250)
    valid_page = len(page) >= 1
    while valid_page:
        for shopify_product in page:
            shopify_product.destroy()
        valid_page = page.has_next_page()
        if valid_page:
            page = page.next_page()


def delete_staging_product(product_id):
    shopify.ShopifyResource.set_site(STAGING_SHOP)
    product = shopify.Product.find(product_id)
    product.destroy()
