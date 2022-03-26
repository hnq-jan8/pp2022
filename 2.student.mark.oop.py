'''
This program has all the same features as the previous one
but it is an OOP version
'''
#   Classes: Student, Course
class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def display_info(self):
        print(f"\t. {self.name}\n\t    ID: '{self.id}'   DoB: {self.DoB}")        

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = []         # list of dict {student_id: mark}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_marks(self):
        return self.marks

    def display_info(self):
        print(f"\t. {self.name}\n\t    ID: '{(self.id).lower()}'")

    def add_student(self, student_id):
        self.marks.append({student_id: -1})

    def update_marks(self, student_id, marks):
        for i in range(len(self.marks)):
            if student_id in self.marks[i]:
                self.marks[i][student_id] = marks

#   Main program
def input_quantity(str):
    # Input number of students
    while True:
        n = (input(f'\nEnter number of {str}: '))
        if n.isdigit():         # Check if input is a natural number
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

def show_marks(course_list):
    # Show marks of students for a selected course
    chosen_course = find_object(course_list, 'course')
    print('')
    print(chosen_course.get_marks())
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
        show_marks(courses)
    elif opt == '0':    # Exit
        print('\n----------------- Bye ------------------\n')
        break
    else:
        print(f'There is no option "{opt}"')