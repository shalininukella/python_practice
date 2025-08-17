class Car:
    wheels = 4
    fuel_types = {"petrol", "diesel", "ev"}

    def __init__(self, brand, model, fuel):
        if fuel not in  Car.fuel_types:
            raise ValueError(f"invalid fuel type. choose from (petrol, diesel, ev)")
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def rangeEstimate(self):
        if self.fuel == "petrol":
            return 600
        elif self.fuel == "diesel":
            return 500
        else:
            return 200
        
    def __str__(self):
        return f"brand is {self.brand}, model is {self.model}, fuel is {self.fuel}"
    
    def __repr__(self):
        return f"Car({self.brand}, {self.model}, {self.fuel})"
    
c1 = Car("Toyota", "Corolla", "petrol")
print(c1)                      # brand is Toyota, model is Corolla, fuel is petrol
print(repr(c1))                # Car(Toyota, Corolla, petrol)
print(c1.rangeEstimate())     # 600

c2 = Car("Tesla", "Model 3", "ev")
print(c2.rangeEstimate())     # 200
print(Car.wheels)
print(Car.fuel_types)
print(c1.fuel_types)

c2.wheels = 6
print(c2.wheels)

Car.wheels = 8
print(c2.wheels)
print(Car.wheels)
print(c1.wheels)
