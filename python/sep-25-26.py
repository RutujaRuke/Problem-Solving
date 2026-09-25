dictonary1 = {'a': 1, 'b': 2, 'c': 3}

for key in dictonary1:
    print(key, dictonary1[key])

for key, values in dictonary1.items():
    print(key, values)

def add(a, b):
    return a + b

print(add(10, 20))

def mul(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(mul(1, 2, 3, 4, 5))

def addition(*args):
    print(args)