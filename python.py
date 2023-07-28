class Student:
    # Create variable in class
    number_of_students = 0
    school = "Online School"
    # Create contructor
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        
        Student.number_of_students += 1
        
    # create function in class
    def fullname_with_major(self):
        return f"{self.first_name} {self.last_name} is a {self.major} major!"
    def fullname_major_school(self):
        return f"{self.first_name} {self.last_name} is a {self.major} go to {self.school}"
    @classmethod
    def set_online_school(cls, new_shool): # for the first argument, we'll use CLS, which stands for class.
        cls.school = new_shool
    @classmethod
    def split_student(cls, student_str):
        first_name, last_name, age = student_str.split(".")
        return cls(first_name, last_name, age)

print(f"Number of students= {Student.number_of_students}")

student_1 = Student("Nguyễn", "Tuấn Anh", "Full Stack")
student_2 = Student("Sáu", "Bảnh", "FrontEnd")
print(f"Number of students= {Student.number_of_students}")

# print(student_1.fullname_with_major())
# print(Student.fullname_with_major(student_2))
# print(student_1.fullname_major_school())
# print(student_1.school)
# print(student_2.school)
# Student.set_online_school("I use Google Hangouts for class!")
# print(student_1.school)
# print(student_2.school)

new_student = "Tài.Lê.Mobile"
student_3 = Student.split_student(new_student)
print(student_3.fullname_with_major())