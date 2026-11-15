import importlib
import math
import pandas as pd

math_module = importlib.import_module("nov-13-26")

result = math_module.subtraction(10, 5)
print(result)

resultone = math_module.multiplication(10, 5)
print(resultone)

resulttwo = math_module.division(10, 5)
print(resulttwo)

print(math.sqrt(16))
print(math.pi)

x = 10
name = float('nan')
not_a_num = float('nan')

print(math.ceil(x))
print(math.isinf(x))
# print(math.isnan(name))
print(math.isnan(not_a_num))  

data = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

print(data)