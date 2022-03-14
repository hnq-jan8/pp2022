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
    print('\n-----  Enter student information:  -----')
    while True:
        n = int(input('\nEnter number of students: '))
        if n > 0:
            break
    student_list = []
    for i in range(0, n, 1):
        print('\nStudent no {}'.format(i + 1))
        id = (input(' Enter student ID: '))
        name = input(' Enter student name: ')
        DoB = input(' Enter student DoB: ')
        
        # dicts
        student_info = {'ID': id, 'Name': name, 'DoB': DoB}
        student_list.append(student_info)

    return student_list

def input_course_info():
    # Input number of courses
    # Input course information: id, name
    print('\n-----  Enter course information:  -----')
    while True:
        n = int(input('\nEnter number of courses: '))
        if n > 0:
            break
    courses_list = []
    for i in range(0, n, 1):
        print('\nCourse no {}'.format(i + 1))
        id = (input(' Enter course ID: '))
        name = input(' Enter course name: ')
        
        course_info = {'ID': id, 'Name': name}
        courses_list.append(course_info)

    return courses_list

def input_marks(course_list, student_list):
    # Select a course, input marks for student in this course
    print('\n-----  Enter marks for students:  -----')
    while True:
        course_id = (input('\nEnter course ID to update students marks: '))
        if course_id in [x['ID'] for x in course_list]:
            course_name = [x['Name'] for x in course_list if x['ID'] == course_id][0]
            break
        else:
            print('Invalid course ID!')

    for i in range(0, len(student_list), 1):
        # student_id = student_list[i]['ID']
        student_name = student_list[i]['Name']
        while True:
            marks = int(input('\nEnter marks of {} for student {} (1, 20): '.format(course_name, student_name)))
            if marks >= 0 and marks <= 20:
                print('{} marks for {} in {} is {}'.format(student_name, course_name, course_id, marks))
                student_list[i].update({course_name: marks})
                break
            else:
                print('Invalid marks!')

student_list = input_student_info()
course_list = input_course_info()

while True:
    opt = input('\n----------------------------------------\n\nChoose an option:\n  1. List courses\n  2. List students\n  3. Update course marks\n  4. Show student marks for a given course\n  5. Exit\n\nYour choice: ')
    if opt == '1':    # List courses
        print('\n----------------------------------------\n\n\tCourses list:')
        for i in range(0, len(course_list), 1):
            print('\t. {}   ID: {}'.format(course_list[i]['Name'], course_list[i]['ID']))
    elif opt == '2':  # List students
        print('\n----------------------------------------\n\n\tStudents list:')
        for i in range(0, len(student_list), 1):
            print('\t. {}  ID: {}  DoB: {}'.format(student_list[i]['Name'], student_list[i]['ID'] , student_list[i]['DoB']))
    elif opt == '3': # Input course marks
        input_marks(course_list, student_list)
    elif opt == '4':
        while True:
            course_id = (input('\n----------------------------------------\n\nEnter course ID to show students marks: '))
            if course_id in [x['ID'] for x in course_list]:
                course_name = [x['Name'] for x in course_list if x['ID'] == course_id][0]
                break
            else:
                print('Invalid course ID!')
        for i in range(0, len(student_list), 1):
            if course_name in student_list[i]:
                print(' {} has {} marks in {}'.format(student_list[i]['Name'], student_list[i][course_name], course_name))
            else:
                print(' {} has no marks in {}'.format(student_list[i]['Name'], course_name))
    elif opt == '5':
        break
    else:
        print('Invalid option!')