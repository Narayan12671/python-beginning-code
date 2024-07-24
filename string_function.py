class detail:
    def __init__(hello, name, age, gender):
        hello.name = name
        hello.age = age
        hello.gender = gender
    def function(manxe):
        print("my name is " +  manxe.name)
        print(manxe.age)
        print("i am " +  manxe.gender)
p = detail("Narayan", 26, "male")
p.function()