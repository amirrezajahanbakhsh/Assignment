name1 = input("enter name: ")
name2 = input("enter name: ")
name3 = input("enter name: ")
name4 = input("enter name: ")
name5 = input("enter name: ")
name6 = input("enter name: ")
name7 = input("enter name: ")
name8 = input("enter name: ")
name9 = input("enter name: ")
name10= input("enter name: ")

letter = input("enter your letter ")

name11 = name1.count(letter)
name12 = name2.count(letter)
name13 = name3.count(letter)
name14 = name4.count(letter)
name15 = name5.count(letter)
name16 = name6.count(letter)
name17 = name7.count(letter)
name18 = name8.count(letter)
name19 = name9.count(letter)
name20 = name10.count(letter)

sum = name11 + name12 + name13 + name14 + name15 + name16 + name17 + name18 + name19 + name20

print("in", name1.title(), "is", name11, letter)
print("in", name2.title(), "is", name12, letter)
print("in", name3.title(), "is", name13, letter)
print("in", name4.title(), "is", name14, letter)
print("in", name5.title(), "is", name15, letter)
print("in", name6.title(), "is", name16, letter)
print("in", name7.title(), "is", name17, letter)
print("in", name8.title(), "is", name18, letter)
print("in", name9.title(), "is", name19, letter)
print("in", name10.title(),"is", name20, letter)
print("at all", letter, "reapiting by", sum)