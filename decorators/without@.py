def add_greet(func):
    def wrapper():
        print("hi!")
        func()
        print("bye!")
    return wrapper

def say_name():
    print("shalini")

decorated_func = add_greet(say_name)
decorated_func()
say_name()
