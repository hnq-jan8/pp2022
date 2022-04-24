from domains.Entity import Entity

class Course(Entity):
    def __init__(self, id = None, name = None, credits = None):
        if id == None:
            super().__init__()
            c = input('. Enter course credits: ')
            while not c.isdigit() or int(c) < 1:
                c = input(f'''  (!) Invalid number for credits
                    \r     Enter again course credits: ''')
            self.__credits = int(c)
        else:
            self.set_id(id)
            self.set_name(name)
            self.__credits = int(credits)

    def __repr__(self):
        return f"Course('{self.get_id()}', '{self.get_name()}', '{self.__credits}')"

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f'''\t. {self.get_name()}
            \r\t    ID: '{self.get_id().lower()}' \t Credits: {self.__credits}'''