# -*- coding: utf-8 -*-


from utils import dist


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

    def closest_warehouse(self, drone, offer):
        potential_warehouses = (w for w in self.warehouses if w.has_product([offer["product"]], offer["count"]))
        assert len(potential_warehouses) > 0
        return min(self.warehouses, key=lambda w: dist(w.pos, drone.pos))
