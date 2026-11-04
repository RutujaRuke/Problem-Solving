tuple = (1, 2, 3, 4, 5)

for i in tuple:
    print(i)

tuple1 = list(tuple)
tuple1.append(6)
tuple2 = tuple(tuple1)

for i in tuple2:
    print(i)

