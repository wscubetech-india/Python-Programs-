num = int(input('enter a number here: '))

if num < 0:
    print ("the natural numbers are greater than 0")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print ("the sum of natural numbers upto the given number is",sum)

