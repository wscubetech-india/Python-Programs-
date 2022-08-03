num1 = int(input("enter a number here: "))
num2 = int(input("enter a number here: "))
num3 = int(input("enter a number here: "))

if (num1 > num2) and (num1 > num3):
    print (num1,"is the greatest among all")
elif (num2 > num1) and (num2 > num3):
    print(num2, "is the greatest among all")
else:
    print(num3, "is the greatest among all")
