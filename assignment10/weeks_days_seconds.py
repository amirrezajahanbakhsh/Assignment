from datetime import date
today = date.today()
day = int(input("enter your day of birth: "))

month = int(input("enter your month of birth: "))

year = int(input("enter your year of birth: "))

days = (today.year - year) * 365 + (today.month - month) * 30 + today.day - day
weeks = days / 7
seconds = ((days * 24) * 60) * 60
print("weeks = ", weeks)
print("days = ", days)
print("seconds = ", seconds)