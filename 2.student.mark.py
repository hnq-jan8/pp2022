'''
This program has all the same features as the previous one
but it is an OOP version
'''
# Classes: Student, Course

class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_DoB(self):
        return self.DoB

    def display_info(self):
        print(f'\t. {self.name}\n\t     ID: {self.id}   DoB: {self.DoB}')

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def display_info(self):
        print(f'\t. {self.name}\n\t     ID: {self.id}')

#   Main program

def input_student_number():
    # Input number of students
    while True:
        n = (input('\nEnter number of students: '))
        if n.isdigit():   # Check if input is a natural number
            n = int(n)
            if n > 0:
                break
            else: print('Invalid number!')
        else: print('Invalid number!')
    return n

def input_course_number():
    # Input number of courses
    while True:
        n = (input('\nEnter number of courses: '))
        if n.isdigit():   # Check if input is a natural number
            n = int(n)
            if n > 0:
                break
            else: print('Invalid number!')
        else: print('Invalid number!')
    return n

def check_exist_ID(id, list):
    # Check if ID already exists
    for i in list:
        if i.get_id() == id:
            return True
    return False

def input_student_info(n):
    # Input student information: id, name, DoB
    print('\n-----  Enter student information:  -----')
    student_list = []
    for i in range(0, n, 1):
        print('\nStudent no {}'.format(i + 1))
        id = input('. Enter student ID: ').upper()

        while check_exist_ID(id, student_list) == True:
            id = (input('''  This ID is already taken
            \r  Enter again student ID: ''')).upper()
        name = input('. Enter student name: ')
        DoB = input('. Enter student DoB: ')
        
        student = Student(id, name, DoB)
        student_list.append(student)
    return student_list

def input_course_info(n):
    # Input course information: id, name
    print('\n-----  Enter course information:  -----')
    course_list = []
    for i in range(0, n, 1):
        print('\nCourse no {}'.format(i + 1))
        id = input('. Enter course ID: ').upper()

        while check_exist_ID(id, course_list) == True:
            id = (input('''  This ID is already taken
            \r  Enter again course ID: ''')).upper()
        name = input('. Enter course name: ')

        course = Course(id, name)
        course_list.append(course)

def display_list(list):
    # Show the list of students
    for i in list:
        i.display_info()

studentCount = input_student_number()
courseCount = input_course_number()
students = input_student_info(studentCount)
courses = input_course_info(courseCount)

while True:
    opt = input('''
        \r----------------------------------------\n
        \rChoose an option:
        \r  1. List courses
        \r  2. List students
        \r  3. Update course marks
        \r  4. Show student marks for a given course
        \r  0. Exit\n
        \rYour choice: ''')

    if opt == '1':      # List courses
        print('\n----------------------------------------\n\n\tCourses list:')
        display_list(courses)
    elif opt == '2':    # List students
        print('\n----------------------------------------\n\n\tStudents list:')
        display_list(students)
    elif opt == '3':    # Input course marks
        # input_marks(course_list, student_list)
        break   # Delete this now!
    elif opt == '4':    # Show student marks for a given course
        # show_marks(course_list, student_list)
        break   # Delete this now!
    elif opt == '0':    # Exit
        print('\n----------------- Bye ------------------\n')
        break
    else:
        print('Invalid option!')