list = ('1', '12', '123')

tuple = ['1', '23', '322']

value = range(3, 10, 3)

print(type(list))
print(type(tuple))
print(type(value))

for i in value:
    print(i)

# -------- function -------------

def name(name):
    print(f"my name is {name}")

value = name("Ritu")

def add(a, b):
    print(f"sum of {a} and {b} is {a + b}")

value2 = add(10, 20)

def create_user(name, role="user"):
    print(f"user name {name} and role is {role}")

v1 = create_user('Rutuja', 'admin')
v2 = create_user('Rutuja') 

card = []

def add_item(item, cart=[]):
    card.append(item)
    return cart

print(add_item('apple'))
print(add_item('banana'))
print(add_item('cherry'))