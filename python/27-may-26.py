# modules
n = 7
print(n % 2)

# floor division
print(7 // 2)
print(7 / 2)
# -----------------------------------
age = 22
has_id = True
print(age >= 25 and has_id)
print(age >= 25 or has_id)
print(not has_id)

# if -else statement

mark = 75
if(mark >= 90):
    print("Grade A")
elif(mark >= 70):
    print("Grade B")
elif(mark >= 60):
    print("Grade C")
else:
    print("Grade F")
# ---------------------------------
num1 = 10
if(num1 > 0):
    print("the number is positive")
elif(num1 < 0):
    print("the number is negative")
else:
    print("the number is zero")
# ---------------------------------
year = 2019
if(year % 4 == 0):
    print("leap year")
else:
    print('not leap year')
# ----------------------------------
a = 10
b = 2234
c = 30
if(a > b and a > c):
    print("a is large number")
elif(b > a and b > c):
    print("b is large number")
else:
    print("c is large number")
# -----------------------------------
count = 4
while count <= 5:
    print(count)
    count += 1

