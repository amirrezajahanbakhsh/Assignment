class Cup:
    def __init__(self,color):
        self_color = color #proteced variable
        self.__content = None #private variable
        
    def fill(self,beverage):
        self.__content = beverage
        
    def empty(self):
        self.__content = None 