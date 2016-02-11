# encoding: utf-8


class Drone:

    def __init__(self, pos=None, products=None, max_payload=-1, id=None):
        self.id = id
        self.pos = pos
        self.busy_time = -1
        self.products = products
        self.max_payload = max_payload
        self.end_state = "warehouse"  # where the drone will be after a delivery

    def busy(self, turn):
        return turn > self.busy_time

    def remaining_weight(self):
        w = 0
        for item in self.items:
            w += self.products[item]

        return self.max_payload - w
