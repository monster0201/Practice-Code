"""Problem Description
Given an integer A, determine whether it is palindromic or not.
A palindrome integer is an integer X for which reverse(X) = X where 
reverse(X) is X with its digits reversed. For e.g., reverse(123) = 321.
"""


n = int(input())
temp = n
    #print(temp)
rev_n = 0
while n > 0:
        rem = n % 10
       # rev_n += rem
        rev_n = (rev_n * 10) + rem
        n = n // 10
    #print(rev_n)
   # print("n:", n)
if rev_n == temp:
        print("Yes")
else:
        print("No")
