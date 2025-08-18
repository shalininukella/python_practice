dict1 = {"a": 1, "b": 99, "c":3, "d": -3}
maxi = float("-inf")
ans = ""
for k,v in dict1.items():
    if v > maxi:
        maxi = v
        ans = k

print(ans)