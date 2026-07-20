def function(name):
    return f"hello {name}!"

result = function("Ritu")
print(result)

def add(a, b):
    result = a + b
    return result

def add_no_return(a, b):
    result = a + b
    
x = add(2, 3)
y = add_no_return(2, 3)