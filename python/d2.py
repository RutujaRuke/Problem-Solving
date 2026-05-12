# Take a 2 number as input and find their sum, difference, product, and quotient.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# Find the area of a circle given its radius.

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("the area of the circle is:", area)

# Find the area of a rectangle given its length and width.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("the area of the rectangle is:", area)

# Find the area of a triangle given its base and height.

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("the area of the triangle is:", area)

# Find the area of a square given its side length.

side = float(input("Enter the side length of the square: "))
area = side * side
print("the area of the square is:", area)

# Find the area of a parallelogram given its base and height.

base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
area = base * height
print("the area of the parallelogram is:", area)

