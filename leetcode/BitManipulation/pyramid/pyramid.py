from typing import List, Dict


def pyramidTransition(bottom, allowed):
    pyramid: Dict = {}
    for v in allowed:
        if v[:-1] in pyramid:
            pyramid[v[:-1]].append(v[-1])
        else:
            pyramid[v[:-1]] = [v[-1]]

    return dfsT(bottom, "", pyramid)


def dfsT(bottom, above, pyramid):
    if len(bottom) == 2 and len(above) == 1:
        return True
    if len(bottom) == len(above) + 1:
        return dfsT(above, "", pyramid)

    base = bottom[len(above) : len(above) + 2]

    if base in pyramid:
        for key in pyramid:
            if dfsT(bottom, above + key, pyramid):
                return True

    return False
