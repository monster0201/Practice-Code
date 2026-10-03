n=int(input("Enter a number:"))
count=0
while(n>0):
    digit=n%10
    count=count+digit
    n=n//10
print("The total sum of digits is:",count)