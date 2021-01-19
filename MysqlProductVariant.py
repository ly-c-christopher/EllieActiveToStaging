class MysqlProductVariant:
    def __init__(self, id, product_id=None, title=None, price=None, sku=None, position=None, inventory_policy=None,
                 compare_at_price=None, fulfillment_service=None, inventory_management=None, option1=None, option2=None,
                 option3=None, created_at=None, updated_at=None, taxable=None, barcode=None, grams=None, image_id=None,
                 weight=None, weight_unit=None, inventory_item_id=None, inventory_quantity=None,
                 old_inventory_quantity=None, tax_code=None, requires_shipping=None, admin_graphql_api_id=None):
        self.id = id
        self.product_id = product_id
        self.title = title
        self.price = price
        self.sku = sku
        self.position = position
        self.inventory_policy = inventory_policy
        self.compare_at_price = compare_at_price
        self.fulfillment_service = fulfillment_service
        self.inventory_management = inventory_management
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.created_at = created_at
        self.updated_at = updated_at
        self.taxable = taxable
        self.barcode = barcode
        self.grams = grams
        self.image_id = image_id
        self.weight = weight
        self.weight_unit = weight_unit
        self.inventory_item_id = inventory_item_id
        self.inventory_quantity = inventory_quantity
        self.old_inventory_quantity = old_inventory_quantity
        self.tax_code = tax_code
        self.requires_shipping = requires_shipping
        self.admin_graphql_api_id = admin_graphql_api_id

    def format(self):
        return {'title': self.title, 'price': self.price, 'sku': self.sku, 'position': self.position,
                'inventory_policy': self.inventory_policy, 'compare_at_price': self.compare_at_price,
                'fulfillment_service': self.fulfillment_service, 'inventory_management': self.inventory_management,
                'option1': self.option1, 'option2': self.option2, 'option3': self.option3, 'taxable': self.taxable,
                'barcode': self.barcode, 'grams': self.grams, 'weight': self.weight,
                'weight_unit': self.weight_unit, 'inventory_item_id': self.inventory_item_id,
                'tax_code': self.tax_code, 'requires_shipping': self.requires_shipping}

    def to_string(self):
        return 'PRODUCT_VARIANT: [id: %s] [product_id: %s] [title: %s] [price: %s] [sku: %s] [position: %s] [inventory_policy: %s] ' \
               '[compare_at_price: %s] [fulfillment_service: %s] [inventory_management: %s] [option1: %s] ' \
               '[option2: %s] [option3: %s] [created_at: %s] [updated_at: %s] [taxable: %s] [barcode: %s] [grams: %s]' \
               ' [image_id: %s] [weight: %s] [weight_unit: %s] [inventory_item_id: %s] [inventory_quantity: %s] ' \
               '[old_inventory_quantity: %s] [tax_code: %s] [requires_shipping: %s] [admin_graphql_api_id: %s] ' \
               % (self.id, self.product_id, self.title, self.price, self.sku, self.position, self.inventory_policy,
                  self.compare_at_price, self.fulfillment_service, self.inventory_management, self.option1,
                  self.option2, self.option3, self.created_at, self.updated_at, self.taxable, self.barcode, self.grams,
                  self.image_id, self.weight, self.weight_unit, self.inventory_item_id, self.inventory_quantity,
                  self.old_inventory_quantity, self.tax_code, self.requires_shipping, self.admin_graphql_api_id)
