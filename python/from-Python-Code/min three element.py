a = int(input("num1: "))
b = int(input("num2: "))
c = int(input("num3: "))
    
if (a < b) & (a < c):
        print(a)
elif (b < a) & (b < c):
        print(b)
else:
        print(c)