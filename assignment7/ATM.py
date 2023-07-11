password = '1248'
password_list = [password[0],password[1],password[2],password[3]]
counter = 0

while counter < 3:
    input_password = input("please enter your password:  ")
    
    if len(input_password) == 4:
        if password == input_password:
            print("your password is correct")
            exit()
        
        elif str([input_password[0],input_password[1],input_password[2],input_password[3]]) == str(password_list[::-1]):
            print("Calling the police!!")
            exit()
        
        else:
            print("your password is wrong!")
            counter += 1
    
    else:
        print("the number characters in password is low!")

print("lock!")