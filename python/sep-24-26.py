# -----------------Conditions--------------------

marks = 56

if marks >= 48:
    print("pass")
elif marks < 48 and marks >= 35:
    print("reappear")
else:
    print("fail")


# if request.user.is_authenticated:
#     print("user is logged in")
# else:
#     print("user is not logged in")

# if user.is_active:
#     print("user is active")
# else:
#     print("user is not active")

# if product.stock > 0:
#     print("product is available")
# else:
#     print("product is not available")

# ------------------loops--------------------

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ------------------dictionary--------------------

user = { "name": "ritu", "age": 22, "city": "pune" }
for key in user:
    print(key, user[key])

for value in user.values():
    print(value)