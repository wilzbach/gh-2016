# -*- coding: utf-8 -*-


from scipy.spatial import distance
import math


class State:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def next_free_drone(self):
        """ returns the next free drone """
        next_drone = self.drones[0]
        for drone in self.drones:
            if drone.next_busy < next_drone.next_busy:
                next_drone = drone
        return next_drone

    def dist(self, pos1, pos2):
        """ computes the distance between everything """
        poss = [pos1, pos2]
        for i, pos in enumerate(poss):
            # if "pos" in pos:
                # pos[i] = pos["pos"]
            if hasattr(pos, "pos"):
                pos[i] = pos.pos
        d = distance.euclidean(*poss)
        d = math.ceil(d)
        return d

    def closest_warehouse(self, drone, offer):
        potential_warehouses = (w for w in self.warehouses if w.has_product([offer["product"]], offer["count"]))
        assert len(potential_warehouses) > 0
        return min(self.warehouses, key=lambda w: self.dist(w.pos, drone.pos))

    def next_offer(self):
        """ looks at all drones and gives the nearest offer """
        next_drone = self.next_free_drone()
        next_order = None
        current_dist = None
        for order in self.orders:
            if order.has_unreserved_items():
                if next_order is None or self.dist(next_drone, order) < current_dist:
                    next_order = order
                    current_dist = self.dist(next_drone.pos, order.pos)

        item, count = order.best_unreserved_item()
        count = min(int(self.max_payload / self.products[item]), count)
        offer = {"product": item, "order": order, "count": count}
        return offer
