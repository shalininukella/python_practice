# 💡 Key idea:
# args is a tuple inside wrapper.
# *args unpacks that tuple back into individual arguments when calling func.
# Same for **kwargs, except it works with keyword arguments.


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling the function: {func.__name__} with args= {args} and kwargs={kwargs}")
        func(*args, **kwargs)
    return wrapper


def add(a,b):
    print(f"sum is {a+b}") 

decorated_func = decorator(add)
decorated_func(2,3)


