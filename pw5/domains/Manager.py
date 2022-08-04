from input import *
import time


class Manager:
    def input_data(self):
        studentCount = input_quantity('students')
        courseCount = input_quantity('courses')
        students = input_info('student', studentCount)
        courses = input_info('course', courseCount)

        # Create a list courses marks for each student
        for i in students:
            i.add_course(courseCount)

        return students, courses

    def run(self):
        if students_data_exist():
            # If the students.dat is exists, read the data from the file
            print()
            for i in range(0, 5):
                print('Found students.dat. Reading data' + '.'*i, end='\r')
                time.sleep(0.5)
            print()
            try:
                decompress_file()
                students = read_info('student')
                courses = read_info('course')
                print('Data read successfully!')
            except Exception as e:
                print(f'(!) Error: {e}')
                input('\nPress Enter to input data from the beginning...')
                students, courses = self.input_data()
        else:
            students, courses = self.input_data()

        while True:
            calculate_gpa(courses, students)     # Auto calculate GPA and sort
            # Auto save marks info
            write_marks(courses, students)
            write_info('student', students)

            opt = input('''
                \r----------------------------------------\n
                \rChoose an option:
                \r  1. Students list (GPA descending)
                \r  2. Courses list
                \r  3. Update marks
                \r  4. Marks list
                \r  0. Exit\n
                \rYour choice: ''')
            if opt == '1':      # Show students list
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
                # Ask for a compression of all files
                confirm = input('''
                                \rDo you want to save before exit?
                                \rType 'y' for yes: ''').lower()
                if confirm == 'y':
                    compress_files()
                    print('\nSave successfully!')
                else:
                    print('\nExit without saving!')
                print('\n----------------- Bye ------------------\n')
                # Delete all created txt files
                delete_file('students.txt')
                delete_file('courses.txt')
                delete_file('marks.txt')
                break
            else:
                print(f'There is no option "{opt}"')
