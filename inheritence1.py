class calculation:
    def add(self, a, b):
        return a+b       
class calculation1:
    def subtraction(self,a,b):
        return a-b
class calculation2:
    def multiplication(self,a,b):
        return a*b
class derived(calculation, calculation1, calculation2):
    def divide(self, a, b):
        return a/b
obj = derived()
print(obj.add(5,5))
print(obj.subtraction(10,5))
print(obj.multiplication(6,5))
print(obj.divide(20,10))
