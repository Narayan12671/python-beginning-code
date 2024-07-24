class car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model =model
    def move(self):
        print("Drive")
class boat:
    def __init__(self, brand, model) -> None:
        self.barnd = brand
        self.model = model
    def move(sef):
        print("Sail")
class plane:
    def __init__(self, brand, model) -> None:
        self.model = model
        self.brand = brand
    def move(self):
        print("fly")
obj1 = car('Mustang', 'yellow')
obj2 = boat('titanic', 'green')
obj3 = plane('boeing', '747')
for x in (obj1, obj2, obj3):
    x.move()

