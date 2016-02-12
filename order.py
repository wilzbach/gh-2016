#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Order:

    def __init__(self, id=-1, items=None, pos=None):
        self.id = id
        self.items = {}
        self.in_progress = {}
        for item in items:
            if item not in self.items:
                self.items[item] = 0
                self.in_progress[item] = 0
            self.items[item] += 1
        self.pos = pos
        self.done = False

    def is_done(self):
        return sum(self.items.values()) == 0

    def has_unreserved_items(self):
        return sum(self.items.values()) != sum(self.in_progress.values())

    def unreserved_items(self):
        return {key: self.items[key] - self.in_progress[key] for key in self.items.keys() if self.items[key] - self.in_progress[key] != 0}

    def process(self, id, count=1):
        self.in_progress[id] += count

    def complete(self, id, count=1):
        self.items[id] -= count
        self.in_progress[id] -= count
        assert self.items[id] >= 0
        assert self.in_progress[id] >= 0

    def best_unreserved_item(self, max_payload):
        """ any item """
        return max(self.unreserved_items().items(), key=lambda x: x[1])
