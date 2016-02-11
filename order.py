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

    def is_available(self):
        return sum(self.items.values()) != sum(self.in_progress.values())

    def process(self, id, count=1):
        self.in_progress[id] += count

    def complete(self, id, count=1):
        self.items[id] -= count
        self.in_progress[id] -= count
        assert self.items[id] >= 0
        assert self.in_progress[id] >= 0
