class PsqlProduct:
    def __init__(self, shopify_id, body_html=None, handle=None, images=None, options=None, product_type=None,
                 published_at=None, image=None, published_scope=None, tags=None, template_suffix=None, title=None,
                 metafields_global_title_tag=None, metafields_global_description_tag=None, variants=None, vendor=None,
                 created_at=None, updated_at=None):
        self.body_html = body_html
        self.shopify_id = shopify_id
        self.handle = handle
        self.images = images
        self.options = options
        self.product_type = product_type
        self.published_at = published_at
        self.image = image
        self.published_scope = published_scope
        self.tags = tags
        self.template_suffix = template_suffix
        self.title = title
        self.metafields_global_title_tag = metafields_global_title_tag
        self.metafields_global_description_tag = metafields_global_description_tag
        self.variants = variants
        self.vendor = vendor
        self.created_at = created_at
        self.updated_at = updated_at

    def to_string(self):
        return '[shopify_id: %s] [handle: %s] [options: %s] [product_type: %s] [image: %s] ' \
               '[published_scope: %s] [image: %s] [published_scope: %s] [tags: %s] [template_suffix: %s] [title: %s]' \
               '[metafields_global_title_tag: %s] [metafields_global_description_tag]: %s] [variants: %s] ' \
               '[vendor: %s] [created_at: %s] [updated_at: %s]' % \
               (self.shopify_id, self.handle, self.images, self.options, self.product_type, self.published_at,
                self.image, self.published_scope, self.tags, self.template_suffix, self.title,
                self.metafields_global_title_tag, self.metafields_global_description_tag, self.variants, self.vendor,
                self.created_at, self.updated_at)
