def add_greet(fun):
    def wrapper():
        print("hi")
        fun()
        print("bye")
    return wrapper

@add_greet
def say_name():
    print("shalini")

say_name()
say_name()
    