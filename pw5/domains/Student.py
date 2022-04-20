from domains.Entity import Entity

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

    def __str__(self):
        return f'''\t. {self.get_name()}
            \r\t    ID: '{self.get_id()}' \t DoB: {self.__DoB}
            \r\t    GPA: {self.get_gpa()}'''