def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(multiply(2, 3, 4, 5,6))

def addition(**kwargs):
    print(kwargs)
    print(type(kwargs))

addition(name="ritu", age=22, city="pune")

