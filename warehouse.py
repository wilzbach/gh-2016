# encoding: utf-8

class Warehouse:

    def __init__(self, id, pos, items):
        self.id = id
        self.pos = pos
        self.items = items

    def has_product(product_id, count):
        return self.items[product_id] >= count

    def take_product(product_id, count):
        assert(self.items[product_id] >= count)
        self.items[product_id] -= count
