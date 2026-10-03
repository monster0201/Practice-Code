"""Problem Description
Mr. Q has a diary in which a lot of numbers are written.
He wants to know the sum of digits for every number.
Ask Mr. Q about the total numbers written in the diary and then write a code to find the sum of
digits for every number.
Note: Total different Numbers are T and for every number (let's say N) you need to find the Sum of digits."""



                                                                                                                                 
   

    


A = int(input())
for i in range(A):
        n = int(input())
        sum = 0
        while n > 0:
            rem = n%10
            #print(rem)
            sum += rem
            n = n//10
        print(sum)

   
