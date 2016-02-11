# encoding: utf-8


class Drone:

    def __init__(self, pos=None, max_payload=-1, id=None):
        self.id = id
        self.pos = pos
        self.busy_time = -1
        self.max_payload = max_payload

        self.product = -1
        self.next_warehouse = None
        self.next_order = None

    def busy(self, turn):
        return turn > self.busy_time

    def process(self, order, warehouse):
        # find best product within max_payload

    def new_instructions(self):

    # def remaining_weight(self):
        # w = 0
        # for item in self.items:
            # w += self.products[item]

        # return self.max_payload - w
