class ProductTag:
    def __init__(self, product_id, tag=None, active_start='', active_end=None, theme_id=''):
        self.product_id = product_id
        self.tag = tag
        self.active_start = active_start
        self.active_end = active_end
        self.theme_id = theme_id

    def to_string(self):
        return '[product_id: %s] [tag: %s] [active_start: %s] [active_end: %s] [theme_id: %s]' % \
               (self.product_id, self.tag, self.active_start, self.active_end, self.theme_id)
