class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employee_count(self):
        return len(self.employees)

    def __str__(self):
        return f"Company: {self.name}, Employees: {self.get_employee_count()}"

    def printname(self):
        print(f"company name: {self.name}")
        print(f"employees: {self.employees}")

    def __repr__(self):
        return f"Company('{self.name}', {self.employees})"

    def __len__(self):
        return self.get_employee_count()

company1 = Company("TechCorp", ["Alice", "Bob", "Charlie"])
company1.printname()
print(len(company1))

company1.add_employee("David")
company1.printname()
print(len(company1))

company1.__str__()
company1.__repr__()
company1.__len__()