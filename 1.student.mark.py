'''
Build a student mark management system using tuples, dicts, lists (no class/object)

Functions
• Input functions:
    • Input number of students in a class
    • Input student information: id, name, DoB
    • Input number of courses
    • Input course information: id, name
    • Select a course, input marks for student in this course
• Listing functions:
    • List courses
    • List students
    • Show student marks for a given course
'''

def input_student_info():
    # Input number of students in a class
    # Input student information: id, name, DoB
    while True:
        n = int(input('\nEnter number of students: '))
        if n > 0:
            break
    student_list = []
    for i in range(0, n, 1):
        print('\nStudent no {}'.format(i + 1))
        id = int(input('Enter student id: '))
        name = input('Enter student name: ')
        DoB = input('Enter student DoB: ')
        
        # dicts
        student_info = {'ID': id, 'Name': name, 'DoB': DoB}
        student_list.append(student_info)

    # print('\nNo \tID \tName \t\t\tDoB')
    # for i in range(0, n, 1):
    #     print((i + 1), '\t', student_list[i]['ID'], '\t', student_list[i]['Name'], '\t', student_list[i]['DoB'])
    return student_list

def input_course_info():
    # Input number of courses
    # Input course information: id, name
    while True:
        n = int(input('\nEnter number of courses: '))
        if n > 0:
            break
    courses_list = []
    for i in range(0, n, 1):
        print('\nCourse no {}'.format(i + 1))
        id = int(input('Enter course id: '))
        name = input('Enter course name: ')
        
        course_info = {'ID': id, 'Name': name}
        courses_list.append(course_info)

    # print('\nNo \tID \tName')
    # for i in range(0, n, 1):
    #     print((i + 1), '\t', courses_list[i]['ID'], '\t', courses_list[i]['Name'])
    return courses_list

def input_marks(course_list, student_list):
    # Select a course, input marks for student in this course
    while True:
        course_id = int(input('\nEnter course id: '))
        if course_id in [x['ID'] for x in course_list]:
            course_name = [x['Name'] for x in course_list if x['ID'] == course_id][0]
            break
        else:
            print('\nInvalid course id!')
    student_id = int(input('Enter student id: '))
    if student_id in [x['ID'] for x in student_list]:
        student_name = [x['Name'] for x in student_list if x['ID'] == student_id][0]
        marks = int(input('Enter marks (1, 20): '))
        if marks >= 0 and marks <= 20:
            print('\nStudent {} has been added to course {} with marks {}'.format(student_name, course_name, marks))
        else:
            print('\nInvalid marks!')
    else:
        print('\nInvalid student id!')
    

course_list = input_course_info()
student_list = input_student_info()
input_marks(course_list, student_list)
print(student_list)
