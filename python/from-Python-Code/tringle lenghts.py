a = int(input("num1: "))
b = int(input("num2: "))
c = int(input("num3: "))

if (a==b) & (b==c) & (c==a):
    print("equal")
elif (a!=b) & (b!=c):
    print("scalene")
else:
    print("isosceles")
