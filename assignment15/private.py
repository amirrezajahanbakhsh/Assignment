class Cup:
    def __init__(self):
        self._color = color  #protected variable
        self.__content = None #private variable
    
    def file(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

cup = Cup()
cup.content