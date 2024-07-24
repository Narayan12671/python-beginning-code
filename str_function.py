class detail:
    def __init__(self, name, age, gender):
        self.name = name
        self.age =age
        self.gender = gender
    def __str__(self):
        return f"{self.name}\n{self.age}\n{self.gender}"
p = detail("Narayan", 26, "Male")
print(p)