class MysqlProductImage:
    def __init__(self, id, product_id=None, position=None, alt=None, width=None, height=None, src=None,
                 variant_ids=None, admin_graphql_api_id=None):
        self.id = id
        self.product_id = product_id
        self.position = position
        self.alt = alt
        self.width = width
        self.height = height
        self.src = src
        self.variant_ids = variant_ids  # array of variant ids
        self.admin_graphql_api_id = admin_graphql_api_id

    def to_string(self):
        return 'PRODUCT_IMAGE: [id: %s] [product_id: %s] [position: %s] [alt: %s] [width: %s] [height: %s] [src: %s] ' \
               '[variant_ids: %s] [admin_graphql_api_id: %s]' \
               % (self.id, self.product_id, self.position, self.alt, self.width, self.height, self.src,
                  self.variant_ids, self.admin_graphql_api_id)

    def format(self):
        return {'src': self.src}