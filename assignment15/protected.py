class Cup:
    def __init__(self):
        self.color = None
        self._content = None #protected variable
    
    def file(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

# if you see something like this    cup = cup()
                                   #cup._content = "tea"

#access to this variable is protected you should notit from outside the class
