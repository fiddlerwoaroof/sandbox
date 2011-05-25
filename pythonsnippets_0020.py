
def cmp_dicts(dct, dct1):
    cp = set()
    for k in dct.keys():
        if dct[k] != dct1.get(k,None):
            cp.add(k)
    return cp
