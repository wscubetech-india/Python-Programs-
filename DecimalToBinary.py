def ConvertBinary(n):
    if n > 1:
        ConvertBinary(n//2)
    print (n%2, end = "")

n =int(input("enter a number here: "))
print ("The converted value in binary is: ")
ConvertBinary(n)