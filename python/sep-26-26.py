def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(70, 50)) 

def addnum(*args):
    print(args)
    return sum(args)

print(addnum(10,20,30,40))

def department(**kwargs):
    print(kwargs)
    print(type(kwargs))

department(name="Ritu", age=22, city="pune")