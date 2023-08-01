def date(year,month,day,):
    return f"{year}/{month}/{day}"

day = int(input("enter day: "))
month = int(input("enter month: "))
year = int(input("enter year: "))

print("your Date: ",date(month,day,))