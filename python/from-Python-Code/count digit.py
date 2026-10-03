'''Problem Description
Mr. Q has a diary in which he has written a lot of numbers. 
He is confused about the number of digits in every number he has written.
Mr. Q will provide the total different numbers written in the diary and 
then you have to write a code to find the number of digits in every number he has written.

Note: Total different Numbers are T and for every number (let's say N) you need to find the total number of digits.'''



    
n = int(input())
T = int(input())

count_of_digits = 0

while n > 0:
        rem = n % 10
        #print(rem)
        count_of_digits += 1
        n = n // 10
    
print(count_of_digits)
    
    

"""testCases = int(input())    

    for i in range(testCases):

        n = int(input())

        count_of_digits = 0

        if n == 0:

            count_of_digits = 1

        while n > 0:

            rem = n % 10

            #print(rem)

            count_of_digits += 1

            n = n // 10

        print(count_of_digits)

"""


   

   