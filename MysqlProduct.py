class MysqlProduct:
    def __init__(self, id, title=None, body_html=None, vendor=None, product_type=None, created_at=None, handle=None,
                 updated_at=None, published_at=None, template_suffix=None, published_scope=None, tags=None,
                 admin_graphql_api_id=None, variants=None, options=None, images=None, image=None, metafield_id=None,
                 metafields=None):
        self.id = id
        self.title = title
        self.body_html = body_html
        self.vendor = vendor
        self.product_type = product_type
        self.created_at = created_at
        self.handle = handle
        self.updated_at = updated_at
        self.published_at = published_at
        self.template_suffix = template_suffix
        self.published_scope = published_scope
        self.tags = tags
        self.admin_graphql_api_id = admin_graphql_api_id
        self.variants = variants  # array of variants
        self.options = options
        self.images = images  # array of image objects
        self.image = image  # first index of the array object
        self.metafield_id = metafield_id
        self.metafields = metafields  # metafield object
        self.real_image_object = None

    # def __eq__(self, other):

    def to_string(self):
        return 'PRODUCT: [id: %s] [title: %s] [body_html: %s] [vendor: %s] [product_type: %s] [created_at: %s] [handle: %s] ' \
               '[updated_at: %s] [published_at: %s] [template_suffix: %s] [published_scope: %s] [tags: %s] ' \
               '[admin_graphql_api_id: %s] [metafield_id: %s]' \
               % (self.id, self.title, self.body_html, self.vendor, self.product_type, self.created_at, self.handle,
                  self.updated_at, self.published_at, self.template_suffix, self.published_scope, self.tags,
                  self.admin_graphql_api_id, self.metafield_id)
