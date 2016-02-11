from scipy.spatial import distance
import math


cache = {}
def dist_ceil(pos1, pos2):
    """ computes the distance between everything """
    k = (pos1, pos2)
    if k in cache:
        return cache[(pos1, pos2)]
    poss = [pos1, pos2]
    for i, pos in enumerate(poss):
        # if "pos" in pos:
            # pos[i] = pos["pos"]
        if hasattr(pos, "pos"):
            poss[i] = pos.pos
    d = distance.euclidean(*poss)
    d = math.ceil(d)
    cache[(pos1, pos2)] = d
    return d
