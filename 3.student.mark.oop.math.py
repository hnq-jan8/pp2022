'''
This program has all the same features as the previous one
but added some new features:
    - GPA calculation
    - Sorting students by GPA in descending order
    - Student marks is rounded to 1 decimal place
'''
import math
import numpy as np

#   Classes: Student, Course
from abc import ABC, abstractmethod


class Entity(ABC):
    ids = []    # List of used IDs

    @abstractmethod
    def __init__(self):
        id = input(f'. Enter {(type(self).__name__).lower()} ID: ').upper()
        while id in self.ids:
            id = input(f'''  (!) This ID is already taken
                \r     Enter again {(type(self).__name__).lower()} ID: ''').upper()
        self.__id = id
        Entity.ids.append(self.__id)
        self.__name = input(f'. Enter {(type(self).__name__).lower()} name: ')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Student(Entity):
    def __init__(self):     # id, name, DoB, gpa
        super().__init__()
        self.__DoB = input(f'. Enter {(type(self).__name__).lower()} DoB: ')
        self.__marks = []   # List of marks for each course
        self.__gpa = 0

    def add_course(self):
        self.__marks.append(-1)

    def get_marks(self):
        return self.__marks

    def get_gpa(self):
        return self.__gpa

    def update_gpa(self, gpa):
        self.__gpa = gpa

    def update_marks(self, i, mark):
        self.__marks[i] = mark

    def display_info(self):
        print(f'''\t. {self.get_name()}
            \r\t    ID: '{self.get_id()}' \t DoB: {self.__DoB}
            \r\t    GPA: {self.get_gpa()}''')


class Course(Entity):
    def __init__(self):     # id, name, credits
        super().__init__()
        c = input('. Enter course credits: ')
        while not c.isdigit() or int(c) < 1:
            c = input(f'''  (!) Invalid number for credits
                \r     Enter again course credits: ''')
        self.__credits = int(c)

    def get_credits(self):
        return self.__credits

    def display_info(self):
        print(f'''\t. {self.get_name()}
            \r\t    ID: '{self.get_id().lower()}' \t Credits: {self.__credits}''')


def input_quantity(str):
    # Input number of students/courses
    n = input(f'\nEnter number of {str}: ')
    while not n.isdigit() or int(n) < 1:
        n = input(f''' (!) Invalid number for {str}
            \r    Enter again number of {str}: ''')
    return int(n)


def input_info(str, n):
    # Input student/course information
    print(f'\n-----  Enter {str} information:  -----')
    list = []
    for i in range(n):
        print(f'\n{str.capitalize()} {i + 1} of {n}')
        if str == 'student':
            object = Student()
        elif str == 'course':
            object = Course()
        list.append(object)
    return list


def display_list(list, str):
    # Show the list of students
    print(f'''\n----------------------------------------
    \r\n\t{str.capitalize()} list:''')
    for object in list:
        object.display_info()
    input('\nPress Enter to continue...')


def find_object(list, str):
    # Find object in the list using ID
    while True:
        id = input(f'\nEnter {str} ID: ').upper()
        for i, object in enumerate(list):
            if object.get_id() == id:
                return object, i
        print(f'Invalid {str} ID!')


def rounded(number):
    # Round number to 1 decimal places
    number *= 10
    if number - math.floor(number) >= 0.5:
        return math.floor(number + 1) / 10
    return math.floor(number) / 10


def input_marks(course_list, student_list):
    # Input marks for student in a selected course
    print('\n-----  Enter marks for students:  -----')
    chosen_course, c = find_object(course_list, 'course')
    course = chosen_course.get_name()
    print(f'Selected course: {course}')

    for s in student_list:
        while True:
            marks = input(
                f'\nEnter marks for {s.get_id()} ~ {s.get_name()} (0, 20): ')
            try:
                marks = rounded(float(marks))
                if marks >= 0 and marks <= 20:
                    s.update_marks(c, marks)
                    print(f'{s.get_name()} marks for {course} is {marks}')
                    break
                else:
                    print('Invalid marks!')
            except ValueError:      # If input is not a number
                print("It's not a number!")
    input(f"\n--- {course}'s marks are updated! ---\nPress Enter to continue...")


def show_marks(course_list, student_list):
    # Show marks of students for a selected course
    print('''\n----------------------------------------
    \r\n\tMarks list:''')
    for c, course in enumerate(course_list):
        print(f'\t. {course.get_name()}:')
        for students in student_list:
            if students.get_marks()[c] != -1:
                print(
                    f'\t    {students.get_name()}: {students.get_marks()[c]}')
            else:
                print(f'\t    {students.get_name()}: not taken')
    input('\nPress Enter to continue...')


def calculate_gpa(course_list, student_list):
    # Calculate GPA for all students and sort students by GPA in descending order
    GPA_list = np.array([])
    for student in student_list:
        marks = np.array([])
        credits = np.array([])
        for mark, course in zip(student.get_marks(), course_list):
            if mark != -1:
                marks = np.append(marks, mark)
                credits = np.append(credits, course.get_credits())
            else:
                continue
        if credits.sum() != 0:  # If student has taken at least one course
            student.update_gpa(
                rounded((marks * credits).sum() / credits.sum()))
        GPA_list = np.append(GPA_list, student.get_gpa())

    GPA_list = np.sort(GPA_list)[::-1]      # Sort GPA in descending order
    for i in GPA_list:                      # Sort students list by sorted GPA
        for student in student_list:
            if student.get_gpa() == i:
                student_list.append(student)
                student_list.remove(student)
                break


if __name__ == '__main__':

    #   Main program
    studentCount = input_quantity('students')
    courseCount = input_quantity('courses')
    students = input_info('student', studentCount)
    courses = input_info('course', courseCount)

    # Create a list courses marks for each student
    for i in students:
        for j in range(courseCount):
            i.add_course()

    while True:
        opt = input('''
            \r----------------------------------------\n
            \rChoose an option:
            \r  1. Students list (GPA descending)
            \r  2. Courses list
            \r  3. Update marks
            \r  4. Marks list
            \r  0. Exit\n
            \rYour choice: ''')

        if opt == '1':      # Show students list in descending order of GPA
            calculate_gpa(courses, students)
            display_list(students, 'student')
        elif opt == '2':    # Show courses list
            display_list(courses, 'course')
        elif opt == '3':    # Select a course and update marks
            confirm = input('''
                \rYou are going to choose a course and update marks for all students.
                    \rType 'y' to confirm: ''').lower()
            if confirm == 'y':
                input_marks(courses, students)
            else:
                print('\nOperation canceled!')
        elif opt == '4':    # Show marks list
            show_marks(courses, students)
        elif opt == '0':    # Exit
            print('\n----------------- Bye ------------------\n')
            break
        else:
            print(f'There is no option "{opt}"')
