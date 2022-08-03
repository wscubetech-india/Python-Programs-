num1 = int(input('enter number 1 here: '))
num2 = int(input('enter number 2 here: '))
num3 = int(input('enter number 3 here: '))

if (num1 > num2) and (num1>num3):
    print (num1,"is a greatest number")
elif (num2 > num1) and (num2 > num3):
    print (num2,"is a greatest number")
else:
    print (num3,"is a greatest number")
