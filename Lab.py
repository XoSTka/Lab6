class Personnel:
    def __init__(self, id: int, fullname: str):
        self.__id = id
        self.__fullname = fullname

class Teacher(Personnel):
    def __init__(self, id: str, fullname: str):
        super().__init__(id, fullname)