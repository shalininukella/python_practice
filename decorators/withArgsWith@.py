# 💡 Key idea:
# args is a tuple inside wrapper.
# *args unpacks that tuple back into individual arguments when calling func.
# Same for **kwargs, except it works with keyword arguments.

# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @debug
# def add(a, b):
#     return a + b

# print(add(3, 5))

def decorator(fun):
    def wrapper(*args, **kwargs):
        print(f"Printing the original function's name using the __name__ attribute i.e function : '{fun.__name__}', where args={args} and kwargs={kwargs}")
        fun(*args, **kwargs)

    return wrapper

@decorator
def add(a,b):
    print(f"sum is : {a+b}")

add(2,3)

