import os
import math
import zipfile
import numpy as np
from domains.Student import Student
from domains.Course import Course

def students_data_exist():
    # Check if students.dat file exists
    if os.path.exists('students.dat'):
        return True
    return False    

def read_info(str):
    # Read student/course information from a file
    list = []
    with open(f'{str + "s"}.txt', 'r') as file:
        for line in file:
            object = eval(line)
            list.append(object)
    return list

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
    write_info(str, list)
    return list

def write_info(str, list):
    # Write student/course information to a file
    with open(f'{str + "s"}.txt', 'w') as file:
        for object in list:
            file.write(f'{repr(object)}\n')

def display_list(list, str):
    # Show the list of students
    print(f'''\n----------------------------------------
    \r\n\t{str.capitalize()} list:''')
    for object in list:
        print(object)
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
            marks = input(f'\nEnter marks for {s.get_id()} ~ {s.get_name()} (0, 20): ')
            try:
                marks = rounded(float(marks))
                if marks >= 0 and marks <= 20:
                    s.update_marks(c, marks)
                    print(f'{s.get_name()} marks for {course} is {marks}')
                    break
                else: print('Invalid marks!')
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
                print(f'\t    {students.get_name()}: {students.get_marks()[c]}')
            else: print(f'\t    {students.get_name()}: not taken')
    input('\nPress Enter to continue...')

def write_marks(course_list, student_list):
    # Write marks of students for a selected course to a file
    with open('marks.txt', 'w') as file:
        for i, course in enumerate(course_list):
            file.write(f'{course.get_name()}:\n')
            for student in student_list:
                if student.get_marks()[i] != -1:
                    file.write(f'\t{student.get_name()}: {student.get_marks()[i]}\n')
                else: file.write(f'\t{student.get_name()}: not taken\n')

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
            else: continue
        if credits.sum() != 0:  # If student has taken at least one course
            student.update_gpa(rounded((marks * credits).sum() / credits.sum()))
        GPA_list = np.append(GPA_list, student.get_gpa())

    GPA_list = np.sort(GPA_list)[::-1]      # Sort GPA in descending order    
    for i in GPA_list:                      # Sort students list by sorted GPA
        for student in student_list:
            if student.get_gpa() == i:
                student_list.append(student)
                student_list.remove(student)
                break

def compress_files():
    # Compress student.txt, course.txt and marks.txt to a .dat file
    # with open('students.dat', 'wb') as file:
    #     with open('students.txt', 'r') as file1:
    #         file.write(file1.read().encode())
    #     with open ('courses.txt', 'r') as file2:
    #         file.write(file2.read().encode())
    #     with open('marks.txt', 'r') as file3:
    #         file.write(file3.read().encode())

    # Compress student.txt, course.txt and marks.txt to a .zip file using zipfile module
    with zipfile.ZipFile('students.dat', 'w') as file:
        file.write('students.txt')
        file.write('courses.txt')
        file.write('marks.txt')

def decompress_file():
    # Decompress students.dat to students.txt and courses.txt using zipfile module
    with zipfile.ZipFile('students.dat', 'r') as file:
        file.extractall()

def delete_file(filename):
    # Delete a file
    os.remove(filename)