class AlternateProduct:
    def __init__(self, product_title=None, product_id=None, variant_id=None, sku=None, product_collection=None):
        self.product_title = product_title
        self.product_id = product_id
        self.variant_id = variant_id
        self.sku = sku
        self.product_collection = product_collection

    def to_string(self):
        return '[product_title: %s] [product_id: %s] [variant_id: %s] [sku: %s] [product_collection: %s]' % \
               (self.product_title, self.product_id, self.variant_id, self.sku, self.product_collection)
