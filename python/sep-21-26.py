age = 25
print(type(age))

name = "rutuja"
age = 25

print(f"My name is {name} and I am {age} years old.")

fruits = ["apple", "banana", "cherry"]
print(fruits[0])

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

len(fruits)

routes = {name: "Route 1", age: "Route 2"}
for route in routes:
    print(routes[route])

months = ("January", "February", "March")
for month in months:
    print(month)

user = { "name": "Ritu", "age": 25, "city": "Pune" }
print(user["age"])

numbers = { 1,2,3,4,5,5 }
print(numbers)

items = ["apple", "banana", "cherry", "banana"]
unique_items = set(items)
print(unique_items)

age = 20
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# Collection	Example	Main purpose
# List	[1, 2, 3]	Ordered, changeable collection
# Tuple	(1, 2, 3)	Ordered, fixed collection
# Set	{1, 2, 3}	Unique values
# Dictionary	{"name": "Rutuja"}	Key-value data

# LIST
# "I have multiple things."

# TUPLE
# "I have multiple things and they shouldn't change."

# SET
# "I only care about unique things."

# DICTIONARY
# "I have information described by keys."