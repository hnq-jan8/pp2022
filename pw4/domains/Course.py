from domains.Entity import Entity

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