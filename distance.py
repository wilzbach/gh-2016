#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.spatial import distance
import math


def dist(g):
    """ adds a distance array for every warehouse with the distances to all orders """
    for w in g["warehouses"]:
        w["distances"] = []
        for o in g["orders"]:
            d = distance.euclidean(w["pos"], o["pos"])
            d = math.ceil(d)
            w["distances"].append(d)
            if "distances" not in o:
                o["distances"] = []
            o["distances"].append(d)
