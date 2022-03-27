'''
This program has all the same features as the previous one
but it is an OOP version
'''
#   Classes: Student, Course
from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"\t. {self.__name}\n\t    ID: '{self.__id}'")

class Student(Entity):
    def __init__(self, id, name, DoB):
        super().__init__(id, name)
        self.__DoB = DoB

    def display_info(self):
        print(f'''\t. {self.get_name()}
            \r\t    ID: '{self.get_id()}'   DoB: {self.__DoB}''')

class Course(Entity):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__marks = []   # List of dict {student_id: mark}

    def get_marks(self):
        return self.__marks

    def add_student(self, student_id):
        self.__marks.append({student_id: -1})   # -1 is the default mark

    def update_marks(self, student_id, marks):
        for i in range(len(self.__marks)):
            if student_id in self.__marks[i]:
                self.__marks[i][student_id] = marks

#   Main program
def input_quantity(str):
    # Input number of students
    while True:
        n = (input(f'\nEnter number of {str}: '))
        if n.isdigit():     # Check if input is a natural number
            n = int(n)
            if n > 0:
                break
            else: print('Invalid number!')
        else: print('Invalid number!')
    return n

def input_info(str, n):
    # Input student/course information
    print(f'\n-----  Enter {str} information:  -----')
    list = []
    for i in range(0, n, 1):
        print(f'\n{str.capitalize()} no {i + 1}')
        id = input(f'. Enter {str} ID: ').upper()
        while id in [object.get_id() for object in list]:
            id = (input(f'''  (!) This ID is already taken
                \r     Enter again {str} ID: ''')).upper()
        name = input(f'. Enter {str} name: ')

        if str == 'student':    # If entering student information
            DoB = input('. Enter student DoB: ')
            object = Student(id, name, DoB)
        elif str == 'course':   # If entering course information
            object = Course(id, name)        
        list.append(object)
    return list

def display_list(list):
    # Show the list of students
    for object in list:
        object.display_info()
    input('\nPress Enter to continue...')

def find_object(list, str):
    # Find object in the list using ID
    while True:
        id = input(f'\nEnter {str} ID: ').upper()
        for object in list:
            if object.get_id() == id:
                return object
        print(f'Invalid {str} ID!')

def input_marks(course_list, student_list):
    # Input marks for student in a selected course
    print('\n-----  Enter marks for students:  -----')
    chosen_course = find_object(course_list, 'course')
    course_name = chosen_course.get_name()
    print(f'Selected course: {course_name}')
    chosen_student = find_object(student_list, 'student')
    student_name = chosen_student.get_name()
    while True:
        marks = input(f'\nEnter marks of {course_name} for student {student_name} (0, 20): ')
        try:
            marks = float(marks)
            if marks >= 0 and marks <= 20:
                chosen_course.update_marks(chosen_student.get_id(), marks)
                print(f'{student_name} marks for {course_name} is {marks}')
                break
            else: print('Invalid marks!')
        except ValueError:      # If input is not a number
            print("It's not a number!")
    input('\nPress Enter to continue...')

def show_marks(course_list, student_list):
    # Show marks of students for a selected course
    chosen_course = find_object(course_list, 'course')
    print('')
    marks = chosen_course.get_marks()
    course = chosen_course.get_name()
    for i in range(len(marks)):
        for key, value in marks[i].items():
            for j in student_list:
                if j.get_id() == key:
                    student = j.get_name()
                    if value != -1:
                        print(f' {student} marks for {course} is {value}')
                    else: print(f' {student} has not taken {course}')
    input('\nPress Enter to continue...')

studentCount = input_quantity('students')
courseCount = input_quantity('courses')
students = input_info('student', studentCount)
courses = input_info('course', courseCount)

# Create a list of students for each course
for i in courses:
    for j in students:
        i.add_student(j.get_id())

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
        print('''\n----------------------------------------
                \r\n\tCourses list:''')
        display_list(courses)
    elif opt == '2':    # List students
        print('''\n----------------------------------------
                \r\n\tStudents list:''')
        display_list(students)
    elif opt == '3':    # Input course marks
        input_marks(courses, students)
    elif opt == '4':    # Show student marks for a given course
        show_marks(courses, students)
    elif opt == '0':    # Exit
        print('\n----------------- Bye ------------------\n')
        break
    else:
        print(f'There is no option "{opt}"')