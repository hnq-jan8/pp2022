from domains.Entity import Entity

class Student(Entity):
    def __init__(self, id = None, name = None, DoB = None, mark = None):
        if id == None:
            super().__init__()
            DoB = input(f'. Enter {(type(self).__name__).lower()} DoB: ')
            while DoB == '':
                DoB = input('  (!) Student DoB is required! Try again: ')
            self.__DoB = DoB
            self.__marks = []
        else:
            self.set_id(id)
            self.set_name(name)
            self.__DoB = DoB
            self.__marks = mark
        self.__gpa = 0

    # def __repr__(self) -> str:
    #     return f"Student('{self.get_id()}', '{self.get_name()}', '{self.__DoB}', {self.__marks})"

    def add_course(self, num_course):
        for _ in range(num_course):
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