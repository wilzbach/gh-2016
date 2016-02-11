from scipy.spatial import distance
import math


def dist_ceil(pos1, pos2):
    """ computes the distance between everything """
    poss = [pos1, pos2]
    for i, pos in enumerate(poss):
        # if "pos" in pos:
            # pos[i] = pos["pos"]
        if hasattr(pos, "pos"):
            poss[i] = pos.pos
    d = distance.euclidean(*poss)
    d = math.ceil(d)
    return d
