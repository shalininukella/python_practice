# nested = [1, [2, [3, 4]], 5]

def flatten(nested):
    res = []
    for i in nested:
        if isinstance(i, list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

print(flatten([1, [2, [3, 4]], 5]))