import Student
#Create 2 instances of Student
student1 = Student.Student("Cyd", "Robertson", "Jounalism", 55, 3.5, "12345")
student2 = Student.Student("Frank", "Williams", "Soil Sciences", 77, 3.4, "23456")

students = []

students.append(student1)
students.append(student2)

for student in students:
    student.print_student_data()