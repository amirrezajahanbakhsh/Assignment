weight = float(input("enter your weight"))
height = float(input("enter your height"))

bmi = (weight / height ** 2) * 10 ** 4

print(bmi)
if bmi < 18.5:
    print("under weight")
elif 18.5 <= bmi < 25:
    print("normal")
elif 25 <= bmi < 30:
    print("over weight")
elif 30 <= bmi < 35:
    print("obese")
else:
    print("extremely obese")

