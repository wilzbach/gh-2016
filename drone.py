# encoding: utf-8

from utils import dist_ceil


class Drone:

    def __init__(self, pos=None, max_payload=-1, id=None):
        self.id = id
        self.pos = pos
        self.busy_time = -1
        self.max_payload = max_payload

        self.in_progress = None

    def busy(self, turn):
        return self.in_progress is not None or turn <= self.busy_time

    def has_new_instructions(self, turn):
        return self.in_progress is not None and turn > self.busy_time

    def process(self, turn, offer):
        self.in_progress = offer

        product = offer["product"]
        count = offer["count"]
        warehouse = offer["warehouse"]

        cmd = load(self.id, warehouse.id, product, count)

        duration = dist_ceil(self.pos, warehouse.pos)+1
        self.busy_time = turn+duration # -1 müsste minus eins sein aber so gehen wir sicher
        self.in_progress = offer
        warehouse.take_product(product, count)
        order.process(product, count)
        self.pos = warehouse.pos

        return cmd

    def new_instructions(self, turn):
        if self.in_progress is None:
            return None

        product = self.in_progress["product"]
        count = self.in_progress["count"]

        cmd = deliver(self.id, self.in_progress["order"].id, product, count)

        duration = dist_ceil(self.pos, order.pos)+1
        self.busy_time = turn+duration # -1 müsste minus eins sein aber so gehen wir sicher
        self.in_progress = None
        order.complete(product, count)
        self.pos = order.pos

        return cmd
