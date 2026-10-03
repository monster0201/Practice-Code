a = int(input("enter 1st num: "))
b = int(input("enter 2nd num: "))
c = int(input("enter 3rd num: "))
if a > b and a > c:
    print("max num=", a)
elif b > a and b > c:
    print("max num=", b)
else:
    print("max num=", c)