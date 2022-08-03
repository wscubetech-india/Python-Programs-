#Solution-1 Using For Loop
#
# num = int(input('enter a number here: '))
# fact = 1
#
# if num < 0:
#     print ("factorial does not exists")
# if num == 0:
#     print ("factorial of 0 is 1")
# if num > 0:
#     for i in range (1,num+1):
#         fact = fact * i
#     print ("the factorial of the given number is:", fact)


#Solution 2 Using recursion
def fact(num):
    if num == 0:
        return 1
    else:
        return ((num)*fact(num-1))

num = int(input("enter a number here: "))

print (fact(num))





