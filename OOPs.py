class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return self.salary

Rakib = employee('Rakib', 10000)
print(Rakib.salary )
print(Rakib.name)
