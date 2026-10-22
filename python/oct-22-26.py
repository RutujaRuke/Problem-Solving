class Class:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

class1 = Class("Alice")
print(class1.greet())

for i in range(5):
    print(f"Iteration {i + 1}: {class1.greet()}")

