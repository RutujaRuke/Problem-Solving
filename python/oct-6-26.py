class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Animal name: {self.name}")

animal1 = Animal("Dog")
animal1.display()

class Wildanimal:
    # def __init__(self, name, activity):
    #     self.name = name
    #     self.activity = activity

    def animalActivity(self):
        print(f"running")

class Tiger(Wildanimal):

    def animalActivity(self):
        print(f"jumping")

tiger1 = Tiger()
tiger1.animalActivity()

class Petanimal:
    def sound(self):
        print(f"barking")

class Dog(Petanimal):
    def sound(self):
        print(f"jumping")
        super().sound()

dog1 = Dog()
dog1.sound()
