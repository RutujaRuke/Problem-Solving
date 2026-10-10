class Number:
    def __init__(self):
        self.num = 0

    def whole_number(self):
        self.num = int(input("Enter a whole number: "))
        print(f"you entered {self.num}")
        if self.num < 5:
            print("This is a less than 5 number")
        elif self.num > 5:
            print("This is a greater than 5 number")
        else:
            print("This is a 5 number")

number1 = Number()
number1.whole_number()


    