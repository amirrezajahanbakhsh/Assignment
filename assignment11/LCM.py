def LCM(a, b):
   if a > b:
      LCM = a
   else:
      LCM = b

   while(True):
      if((LCM % a == 0) and (LCM % b == 0)):
         break
      LCM += 1

   return LCM


number_1 = int(input("enter your first number\n"))
number_2 = int(input("enter your second number\n"))
print("LCM: ",LCM(number_1, number_2))