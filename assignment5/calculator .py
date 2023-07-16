number = int(input("""1_Celsius to Kelvin
2_Celsius to Fahrenheit
3_Kelvin to Celsius
4_Kelvin to Fahrenheit
5_Fahrenheit to Celsius
6_Fahrenheit to Kelvin`
choose your operation: """))
if 1 <= number <= 6:
    number1 = float(input("enter youre number: "))
   
    if number == 1:
        result = number1 + 273.15
   
    elif number == 2:
        result = (number1 * 1.8) + 32
    
    elif number == 3:
        result = number1 - 273.15
    
    elif number == 4:
        result = (number - 273.15) * 1.8 + 32
   
    elif number == 5:
        result = number1 - 32 * 1.8
    
    else:
        result = (number1 - 32) * 1.8 + 273.15
    print(result)
else:
    print("youre number is not found")