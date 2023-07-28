class Student:
    # Create variable in class
    school = "Online School"
    # Create contructor
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
    # create function in class
    def fullname_with_major(self):
        return f"{self.first_name} {self.last_name} is a {self.major} major!"

student_1 = Student("Nguyễn", "Tuấn Anh", "Full Stack")
student_2 = Student("Sáu", "Bảnh", "FrontEnd")

# print(student_1.fullname_with_major())
# print(Student.fullname_with_major(student_2))
print(student_1.school)