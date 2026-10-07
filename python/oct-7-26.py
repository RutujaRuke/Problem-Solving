class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} is barking")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} is jumping")
        super().sound()

animal1 = Dog("Dog")
animal1.sound()

class Wildanimal:
    school = "Wildlife"
    @classmethod
    def get_school(self):
        return self.school
    
wildanimal1 = Wildanimal()
wildanimal1.get_school()