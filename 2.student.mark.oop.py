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

    def get_DoB(self):
        return self.DoB

    def display_info(self):
        print(f"\t. {self.name}\n\t    ID: '{self.id}'   DoB: {self.DoB}")        

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def display_info(self):
        print(f"\t. {self.name}   ID: '{(self.id).lower()}'")

#   Main program
def input_quantity(str):
    # Input number of students
    while True:
        n = (input(f'\nEnter number of {str}: '))
        if n.isdigit():   # Check if input is a natural number
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
        while id in [i.get_id() for i in list]:
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
    for i in list:
        i.display_info()
    input('\nPress Enter to continue...')

def id_to_name(list, str):
    # Find name in the list using ID
    while True:
        id = input(f'\nEnter {str} ID: ').upper()
        for i in list:
            if i.get_id() == id:
                return i.get_name()
        print('Invalid ID!')

def input_marks(course_list, student_list, marks_list):
    # Input marks for student in a selected course
    print('\n-----  Enter marks for students:  -----')
    course_name = id_to_name(course_list, 'course')
    print(f'Selected course: {course_name}')
    student_name = id_to_name(student_list, 'student')
    while True:
        marks = input(f'\nEnter marks of {course_name} for student {student_name} (0, 20): ')
        try:
            marks = float(marks)
            if marks >= 0 and marks <= 20:
                for i in range(len(marks_list)):
                    if marks_list[i]['Student'] == student_name:
                        marks_list[i][course_name] = marks
                print('{} marks for {} is {}'.format(student_name, course_name, marks))
                break
            else: print('Invalid marks!')
        except ValueError:  # If input is not a number
            print("It's not a number!")
    input('\nPress Enter to continue...')

def show_marks(course_list, marks_list):
    # Show marks of students for a selected course
    course_name = id_to_name(course_list, 'course')
    print('')
    for i in marks_list:
        if course_name in i:
            print(f' {i["Student"]} marks for {course_name} is {i[course_name]}')
        else: print(f' {i["Student"]} has not taken {course_name}')
    input('\nPress Enter to continue...')

studentCount = input_quantity('students')
courseCount = input_quantity('courses')
students = input_info('student', studentCount)
courses = input_info('course', courseCount)

marks = []
for i in students:
    marks.append({'Student': i.get_name()})

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
        input_marks(courses, students, marks)
        # print('\n', marks)
    elif opt == '4':    # Show student marks for a given course
        show_marks(courses, marks)
    elif opt == '0':    # Exit
        print('\n----------------- Bye ------------------\n')
        break
    else:
        print(f'There is no option "{opt}"')