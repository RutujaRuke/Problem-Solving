class Car():
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.name}, {self.model}, {self.year}"

my_car = Car("Toyota", "Camry", 2020)
print(my_car.display_info())

