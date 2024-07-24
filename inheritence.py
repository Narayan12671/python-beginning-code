class person:
    def __init__(self,name,rollno,gender):
        self.name = name
        self.rollno = rollno
        self.gender = gender
    def function(self):
        print(self.name, self.rollno, self.gender)
class student(person):
    def __init__(self, name, rollno, gender, id_no, category, grade):
        super().__init__(name, rollno, gender)
        self.id_no = id_no
        self.category = category
        self.grade = grade
    def others(self):
        print(self.id_no, self.category, self.grade)
student_obj = student("Alice", 201, "Female", 1234, "Category A", "Class 10")
student_obj.function()
student_obj.others()
        