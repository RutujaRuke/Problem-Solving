class student :
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1 = student("ritu", 20, "A")
student1.display_info()



class hotel :
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating

    def display(self):
        print(f"hotel name: {self.name}, location: {self.location}, rating: {self.rating}")

    def is_passed(self):
        if self.rating >= 3.0:
            print("hotel is passed")
        else:
            print("hotel is failed")

hotel1 = hotel("the grand", "pune", 3.4)
hotel1.display()
hotel1.is_passed()

