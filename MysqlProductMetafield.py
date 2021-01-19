class MysqlProductMetafield:
    def __init__(self, id, namespace=None, key=None, value=None, value_type=None, description=None, owner_id=None,
                 created_at=None, updated_at=None, owner_resource=None):
        self.id = id
        self.namespace = namespace
        self.key = key
        self.value = value
        self.value_type = value_type
        self.description = description
        self.owner_id = owner_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.owner_resource = owner_resource

    def format(self):
        return {'namespace': self.namespace, 'key': self.key, 'value': self.value, 'value_type': self.value_type}

    def to_string(self):
        return 'PRODUCT_METAFIELD: [id: %s] [namespace: %s] [key: %s] [value: %s] [value_type: %s] [description: %s] [owner_id: %s] ' \
               '[created_at: %s] [updated_at: %s] [owner_resource: %s]' \
               % (self.id, self.namespace, self.key, self.value, self.value_type, self.description, self.owner_id,
                  self.created_at, self.updated_at, self.owner_resource)
