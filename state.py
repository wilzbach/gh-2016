# -*- coding: utf-8 -*-


class State:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def next_free_drone():
        return 0

    def closest_warehouse(self, drone, offer):
        potential_warehouses = [w for w in self.warehouses if w.has_product([offer["product"]], offer["count"])]
        assert(len(potential_warehouses) > 0)
        return minimum(warehouses, key=lambda w: self.dist(w.pos, drone.pos))
