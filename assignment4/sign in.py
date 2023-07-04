username = "amirreza"
password = "12345678"

username1 = (input("enter your username"))
password1 = (input("enter your password"))

if username1 == username and password1 == password:
    print("login")
elif  username1 == username or password1 == password:
    print("i can not find try agane")
    username1 = (input("enter your username")) 
    password1 = (input("enter your password"))  
    
    if username1 == username and password1 == password:
        print("login")
    else:
        print("i can not find")
else:
    print("i can not find")