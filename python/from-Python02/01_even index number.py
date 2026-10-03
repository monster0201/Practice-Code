word = input('enter word:')
print("string:",word)
l = list(word)
x = l
for i in x[2::5]:
    print(i)
