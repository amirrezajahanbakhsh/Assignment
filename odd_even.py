#number = input("enter your number: ")
#number = str(number)

#even = number.count("0") 
#even = number.count("2")
#even = number.count("4")
#even = number.count("6")
#even = number.count("8")

#odd = number.count("1")
#odd = number.count("3")
#odd = number.count("5")
#odd = number.count("7")
#odd = number.count("9")

#if odd > even:
    #print("the odd number is more")
#elif even == odd:
    #print("odd numbers are equal to even numbers")
#else:
   # print("the even number is more")


  ## OR


number = input("enter your number")
number = str(number)

even = number.count("0") + number.count("2") +  number.count("4") + number.count("6") + number.count("8")
odd = number.count("1") + number.count("3") + number.count("5") + number.count("7") + number.count("9")

if odd > even:
    print("the odd number is more")
elif even == odd:
    print("the even number is more")
else:
    print("odd numbers are equal to even numbers")