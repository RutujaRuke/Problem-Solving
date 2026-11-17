try:
    a = 10
    b = 0
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# ----------------------------------

try:
    number = int(input("Enter a number:"))
    print(f"you entered {number}")

except ValueError:
    print("Invalid Input")

else:
    print("your number is:", number)
    print("program completed")

# -----------------------------------

try:
    file = open("notice.txt", "r")

except FileNotFoundError:
    print("Error: The file 'notice.txt' was not found.")

else:
    content = file.read()
    print(content)
    file.close()