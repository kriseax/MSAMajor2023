import Student
#Create 2 instances of Student
list_of_students = []

try:
    #create a file handler
    file = open("students.csv", "r")

    #create variable to keep track of line in file that we are reading
    line_number = 0
    #read file line by line in for loop
    for line_of_data in file:
        line_number += 1
        #skip first line in csv file
        if line_number == 1:
            continue
        
        #split the line of data at the comma
        student_data = line_of_data.split(",")

        #handle errors in data format. line_of_data should have 6 items
        if len(student_data) != 6:
            raise Exception(f"There is an error in your data file on line {line_number}")
        
        #get student data and create a student object for each student
        first_name = student_data[0]
        last_name = student_data[1]
        major = student_data[2]
        credit_hours = int(student_data[3])
        gpa = float(student_data[4])
        student_id = student_data[5].strip()

        new_student = Student.Student(first_name, last_name, major, credit_hours, gpa, student_id)
        list_of_students.append(new_student)

except Exception as err:
    print(err)


for student in list_of_students:
    student.print_student_data()