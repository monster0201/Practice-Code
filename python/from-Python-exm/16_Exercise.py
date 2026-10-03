num = int(input("Print all odd numbers : "))

print("\nOdd numbers from 1 to", num, "are : ")

for i in range(1, num + 1):

    #Check for odd or not.
    if((i % 2) != 0):
        print(i, end=" ")