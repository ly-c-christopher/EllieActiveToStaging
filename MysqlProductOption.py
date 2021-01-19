class MysqlProductOption:
    def __init__(self, id, product_id=None, name=None, position=None, values=None):
        self.id = id
        self.product_id = product_id
        self.name = name
        self.position = position
        self.values = values  # array of size values

    def to_string(self):
        return 'PRODUCT_OPTION: [id: %s] [product_id: %s] [name: %s] [position: %s] [values: %s]' \
               % (self.id, self.product_id, self.name, self.position, self.values)

    def format(self):
        return {'name': self.name, 'position': self.position, 'values': self.values}
