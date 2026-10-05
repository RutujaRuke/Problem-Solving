class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Hello, {self.name}")

    def name(self):
        return self.name

student1= Student("Ritu")
student1.display()

# print(student1.name())

class Student1:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40

student2 = Student1("Ritu", 50)
student2.display()
print(student2.is_passed())

class Animal:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    pass

class cat(Animal):
    pass

dog = Dog()
cat = cat()
dog.eat()
cat.sleep()