class Vehicle:
    def __init__(self, make, model):
        self._make = make  
        self._model = model 

    def describe(self):
        return f"Vehicle: {self._make} {self._model}"
