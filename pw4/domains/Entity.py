from abc import ABC, abstractmethod


class Entity(ABC):
    ids = []    # List of used IDs

    @abstractmethod
    def __init__(self):
        id = input(f'. Enter {(type(self).__name__).lower()} ID: ').upper()
        while id in self.ids:
            id = input(f'''  (!) This ID is already taken
                \r     Enter again {(type(self).__name__).lower()} ID: ''').upper()
        self.__id = id
        Entity.ids.append(self.__id)
        self.__name = input(f'. Enter {(type(self).__name__).lower()} name: ')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
