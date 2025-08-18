
# dict[key]: Raises KeyError if key not found.

# dict.get(key, default): Returns None or given default value if key not found.

# get(key, default) → Returns the value if key exists, else returns default (does NOT insert key).

# setdefault(key, default) → Returns value if key exists, else inserts key with default and returns it.


d = {"a" : 1}
print(d.get("a"))
print(d.get("b"))
print(d.get("b", 0))
print(d.setdefault("c", 0))
print(d.setdefault("a", 3))
print(d["c"])
print(d)
# print(d["b"]) # KeyError: 'b'

