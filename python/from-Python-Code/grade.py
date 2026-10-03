Marks = int(input("Total num: "))
Percent = (Marks/500)*100
print("Total Marks",Marks, "Percentage", Percent)
if Percent >= 90:
    print("Grade A")
elif Percent >= 80:
      print("Grade B")
elif Percent >= 70:
    print("Grade C")
elif Percent >= 60:
    print("Grade D")
elif Percent >= 40:
    print("Grade E")
elif Percent < 40:
    print("Grade F")
else:
    print("none")    