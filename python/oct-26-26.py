class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def update_age(self, new_age):
        self.age = new_age

    def get_age(self):
        return self.age

student1 = student("Ritu", 20)
student1.display()
student1.update_age(21)
print(f"Updated Age: {student1.get_age()}")
