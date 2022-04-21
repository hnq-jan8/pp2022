import input as ip

class Manager:
    def run(self):
        if ip.is_students_data_exist():
        # If the students.dat is exists, read the data from the file
            students = ip.read_info('students')
            courses = ip.read_info('courses')


        else:
            studentCount = ip.input_quantity('students')
            courseCount = ip.input_quantity('courses')
            students = ip.input_info('student', studentCount)
            courses = ip.input_info('course', courseCount)

            # Create a list courses marks for each student
        for i in students:
            for _ in range(len(courses)):
                i.add_course()

        while True:
            ip.calculate_gpa(courses, students)     # Auto calculate GPA and sort
            ip.write_marks(courses, students)       # Auto save marks to a file

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
                ip.display_list(students, 'student')
            elif opt == '2':    # Show courses list
                ip.display_list(courses, 'course')
            elif opt == '3':    # Select a course and update marks
                confirm = input('''
                    \rYou are going to choose a course and update marks for all students.
                        \rType 'y' to confirm: ''').lower()
                if confirm == 'y':
                    ip.input_marks(courses, students)
                else: 
                    print('\nOperation canceled!')
            elif opt == '4':    # Show marks list
                ip.show_marks(courses, students)
            elif opt == '0':    # Exit
                # Ask for a compression of all files
                confirm = input('''
                    \rDo you want to compress all files?
                        \rType 'y' to confirm: ''').lower()
                if confirm == 'y':
                    ip.compress_files()
                print('\n----------------- Bye ------------------\n')
                break
            else:
                print(f'There is no option "{opt}"')