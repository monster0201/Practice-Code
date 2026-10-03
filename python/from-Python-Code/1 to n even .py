'''Write a program to print all even numbers from 1 to N where you have to take N as input from user.'''



A = int(input("num:"))
c = 1
while c <= A:
     if c % 2 == 0:
            print(c, end = ' ')
     c = c + 1
    