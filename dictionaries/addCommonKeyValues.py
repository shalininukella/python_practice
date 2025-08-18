def commonKeySum():
    d1 = {"a": 1, "b": 2}
    d2 = {"a": 3, "c": 4}
    res = {}
    #union of 2 set(dict)
    for k in set(d1) | set(d2):
        res[k] = d1.get(k, 0) + d2.get(k, 0)
    return res

print(commonKeySum())
