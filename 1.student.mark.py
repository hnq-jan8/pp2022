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
        while id in [x['ID'] for x in list]:    # Check if ID is not duplicate
            id = (input(f'  (!) This ID is already taken\n     Enter again {str} ID: ')).upper()
        name = input(f'. Enter {str} name: ')
        
        if str == 'student':      # If entering student information
            DoB = input('. Enter student DoB: ')
            object = {'ID': id, 'Name': name, 'DoB': DoB}
        elif str == 'course':
            object = {'ID': id, 'Name': name}
        list.append(object)
    return list

def id_to_name(list, str):
    # Find name using ID
    while True:
        element_id = (input(f'\nEnter {str} ID: ')).upper()
        
        if element_id in [x['ID'] for x in list]:
            element_name = [x['Name'] for x in list if x['ID'] == element_id][0]
            break
        else:
            print(f'Invalid {str} ID!')
    return element_name

def input_marks(course_list, student_list):
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
                print('{} marks for {} is {}'.format(student_name, course_name, marks))
                for i in range(0, len(student_list), 1):
                    if student_list[i]['Name'] == student_name:
                        student_list[i][course_name] = marks
                break
            else: print('Invalid marks!')
        except ValueError:  # If input is not a number
            print("It's not a number!")

    input('\nPress Enter to continue...')

def show_list_courses(course_list):
    # Show the list of courses
    for i in range(0, len(course_list), 1):
        print("\t. {}   ID: '{}'".format(course_list[i]['Name'], (course_list[i]['ID']).lower()))
    input('\nPress Enter to continue...')

def show_list_student(student_list):
    # Show the list of students
    for i in range(0, len(student_list), 1):
        print(f"\t. {student_list[i]['Name']}\n\t    ID: '{student_list[i]['ID']}'   DoB: {student_list[i]['DoB']}")
    input('\nPress Enter to continue...')

def show_marks(course_list, student_list):
    # Show student marks for a selected course
    course_name = id_to_name(course_list, 'course')
    print('')
    for i in range(0, len(student_list), 1):
        student_name = student_list[i]['Name']
        if course_name in student_list[i]:
            marks = student_list[i][course_name]
            print(' {} marks for {} is {}'.format(student_name, course_name, marks))
        else:
            print(' {} has not taken {}'.format(student_name, course_name))

    input('\nPress Enter to continue...')

studentCount = input_quantity('students')
courseCount = input_quantity('courses')
student_list = input_info('student', studentCount)
course_list = input_info('course', courseCount)

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
        show_list_courses(course_list)
    elif opt == '2':    # List students
        print('\n----------------------------------------\n\n\tStudents list:')
        show_list_student(student_list)
    elif opt == '3':    # Input course marks
        input_marks(course_list, student_list)
    elif opt == '4':    # Show student marks for a given course
        show_marks(course_list, student_list)
    elif opt == '0':    # Exit
        print('\n----------------- Bye ------------------\n')
        break
    else:
        print(f'There is no option "{opt}"')