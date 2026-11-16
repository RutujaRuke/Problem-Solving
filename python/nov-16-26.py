a = 20
b = 0

# result = a / b
# print(result)


try:
    x = 10
    y = 0
    result = x / y
    print(result)
except ZeroDivisionError:
    print("error occurred")

print('program completed')

try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

print('program completed')


try:
    number = 10 / 2

    print(number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Execution completed.")