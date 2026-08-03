def get_value():
    return 5, "Ritu", "pune"

age, name, address = get_value()
print(age)
print(name)
print(address)

def create_user(name, role="user"):
    print(f"User name is {name} and role is {role}")

print(create_user("Ritu"))
print(create_user("Ritu", "admin"))

# Note: never use a mutable object (list/dict) as a default value: -----------------------------------

