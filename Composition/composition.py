class Engine:
    def start(self):
        print("Vehical is starting")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("now start driving")

c = Car()
c.drive()