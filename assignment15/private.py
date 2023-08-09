# class Cup:
#     def __init__(self, color):
#         self._color = color  #protected variable
#         self.__content = None #private variable
    
#     def file(self, beverage):
#         self.__content = beverage

#     def empty(self):
#         self.__content = None

# Now you can fill and empty your
#  cup outside the class only through methods.
#  If you try to use __content from outside 
# the class, you will get an error. However
#, you can work around this error as follows:

# if you see something like this, say to your self: hey, you are wrong
# redcup = Cup("red")
# redcup._Cup__content = "tea"


class Password:
    def __init__(self):
        self.__password = "@amirrezajahnbakhsh123"

    def check_password(self, user_password):
        if self.__password == user_password:
            return True
        else:
            return False

p = Password()
user_password = input("enter password: ")
print(p.check_password(user_password))
print(p.__password)
print(p.password)