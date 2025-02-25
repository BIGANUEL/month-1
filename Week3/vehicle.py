class Vehicle:
    def __init__(self, make, model):
        self._make = make  
        self._model = model  

    def describe(self):
        return f"Vehicle: {self._make} {self._model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors  

    def describe(self):
        return f"Car: {self._make} {self._model}, Doors: {self._num_doors}"

class Bike(Vehicle):
    def describe(self):
        return f"Bike: {self._make} {self._model}"

# Demonstrating polymorphism
vehicles = [
    Car("Toyota", "Camry", 4),
    Bike("Yamaha", "YZF-R3"),
    Vehicle("Generic", "ModelX")
]

for vehicle in vehicles:
    print(vehicle.describe())
