nested = {"a": {"b": {"c": 1}}, "d": 2}

def flaten(nested, parent = "", res = {}):
    for key, val in nested.items():
        prop = f"{parent}_{key}" if parent else key
        if isinstance(val, dict):
            flaten(nested[key], prop, res)
        else:
            res[prop] = val
    return res

print(flaten(nested))
