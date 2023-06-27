import Student
from datetime import datetime

"""
Function to write to error log file
Input: error message
Output: None
"""
def write_to_error_log(message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write error message to log file
        log_file.write(f"{datetime.now()}: {message}\n")
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
        return
    
    return

"""
Function to return list of student objects
Input: none
Output: list of student objects
"""
def load_students():
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
            #if error in format then write a message to a log file and continue reading from the file
            try:
                if len(student_data) != 6:
                    raise Exception(f"There is an error in your data file on line {line_number}")
            except Exception as err:
                write_to_error_log(str(err))
                continue

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

    return list_of_students

"""
Function to convert student object to student dictionaries
Input: List of Student objects
Output: List of student dictionaries
"""
def student_to_dictionary(list_of_students):
    #create a list to store the dictionaries
    student_dictionary_list = []

    #loop through student list and write each student's data to a dictionary
    for student in list_of_students:
        student_dictionary = {}
        #Set heys and values for first name, last, name, ID, major, gpa, class level
        student_dictionary['id'] = student.get_ID()
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()

        #Append to student_dictionary_list
        student_dictionary_list.append(student_dictionary)
    
    return student_dictionary_list

"""
Function to get student dictionaries
Input: none
Output: list of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries

