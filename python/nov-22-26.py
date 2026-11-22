# print(file.readline())
# print(file.readline())
# print(file.readline())



# file1 = open("notice.txt", "w")
# file1.write("I am waiting on grand line")
# file1.close()

# file2 = open("notice.txt", "a")
# file2.write(" Where are you?")
# file2.close()

file = open("notice.txt", "r")

lines = file.readlines()
print(lines)

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "notice.txt"
with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)

import json 
student = {
    'name': 'Ritu',
    'age': 22,
}
data = json.dumps(student)
print(data)
print(type(data))

json_data = '{"name": "Ritu", "age": 22}'
student1 = json.loads(json_data)
print(student1)
print(type(student1))

print(student1['name'])

student3 = {
    'name': 'Ritu',
    'age': 22,
}

with open("student.json", "w") as file:
    json.dump(student3, file, indent=4)

print("Data written to student.json file successfully.")