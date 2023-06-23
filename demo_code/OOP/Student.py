#Create a student Class with these attributes
#First name
#last name
#major
#credit hours (freshman, sophomore, junior, senior)
#gpa
#ID number
#create get/set methods where appropriate
class Student:
    def __init__(self, first_name, last_name, major, credit_hours, gpa, ID):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__ID = ID
        #self.__class_level = sel.
    
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, new_fname):
        self.__first_name = new_fname

    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, new_lname):
        self.__last_name = new_lname

    def get_major(self):
        return self.__major
    
    def set_major(self, new_major):
        self.__major = new_major

    def get_credit_hours(self):
        return self.__credit_hours

    def set_credit_hours(self, new_credits):
        self.__credit_hours = new_credits
    
    def update_credit_hours(self, new_credits):
        self.__credit_hours += new_credits
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa
    
    def get_ID(self):
        return self.__ID

    def get_class_level(self):
        if self.__credit_hours > 90:
            return "Senior"
        elif self.__credit_hours > 60:
            return "Junior"
        elif self.__credit_hours > 30:
            return "Sophomore"
        else:
            return "Freshman"
    
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__ID}\n")