def s_n(n):
    return f"{n}{n+n}{n+n+n}"

n = int(input("enter your number for sequence: "))
print(s_n(n))