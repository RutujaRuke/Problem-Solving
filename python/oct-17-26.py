class Company:

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def printname(self):
        print(f"company name: {self.name}")
        print(f"employees: {self.employees}")

company1 = Company("Techcorp", 100)
company1.printname()










