"""Problem Description
For a given number A, print its multiplication table having the first 10 multiples."""


n = int(input("enter num:"))

c = 1
while c <= 10:
        r = c * n
        print(n, '*', c, '=', r , end='\n ')
        c += 1
