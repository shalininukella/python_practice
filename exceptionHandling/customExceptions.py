class MyError(Exception):
    pass

def func(x):
    if x < 0:
        raise MyError("Negative value not allowed")

try:
    func(-1)
except MyError as e:
    print(f"Caught custom error: {e}")
