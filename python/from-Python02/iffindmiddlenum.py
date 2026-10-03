a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
c=int(input("enter 3rd num"))
if(a>b and a<c) or (a<b and a>c):
    print("middle num=",a)
elif(b>a and b<c) or (b<a and b>c):
    print("middle num=",b)
else:
    print("middle num=",c)
