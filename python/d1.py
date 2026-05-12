#add two numbers 

num1 =10
num2 =20
sum = num1 + num2

print("the sum of the number is:", sum)

#find even and odd number

num = 15

if num % 2 == 0:
    print("the number is even", num)
else:
    print("the number is odd", num)

#find the largest number among three numbers

num1 = 10
num2 = 20
num3 = 30

if num1 >= num2 and num1 >= num3:
    print("the largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("the largest number is:", num2)
else:
    print("the largest number is:", num3)

#find the factorial of a number

num = 5
factorial = 1
if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i

    print("the factorial of", num, "is", factorial)

#find the fibonacci sequence

number = int(input("enter the number of terms:"))
n1 = 0
n2 = 1
count = 0

if number <= 0:
    print("please enter a positive integer")
elif number == 1:
    print(n1)
else:
    print("fabonacci series:")
    while count < number:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        

#find the prime number

num = 29

if num > 1:
    for i in range(1, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:       
        print(num, "is a prime number")
else:    
    print(num, "is not a prime number")

#swap two numbers

num1 = 10
num2 = 20

print("the value of num1 before swapping:", num1)
print("the value of num2 before swapping:", num2)

num1, num2 = num2, num1

print("the value of num1 after swapping:", num1)
print("the value of num2 after swapping:", num2)

#print number from 1 to 10 

i = 1
while i <=10:
    print(i)
    i += 1


for i in range(1, 11):
    print(i)

#find the sum of natural numbers