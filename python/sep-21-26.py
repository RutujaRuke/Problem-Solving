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