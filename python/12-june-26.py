# while True:
#     command = input("enter 'quit' to exit")
#     if command == "quit":
#         break
#     print("you enterd:", command)
# print("exit the loop")

for i in range(1, 11):
    print(i)

items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

for letter in "Rutuja":
    print(letter)

total = 0
for i in range(1, 6):
    total += i
print(total)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)