def fact(n):
    if n == 1:
        return 1
    else:
        return (n*(fact(n-1)))

n = int(input('enter a number here: '))

if n <=0:
    print ("enter a positive number")
else:
    print ('The factorial of the given number is',fact(n))