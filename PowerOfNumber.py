#Solution 1 using while loop

# base = int(input("enter a base number here: "))
# exponent = int(input("enter exponent here: "))
#
# result = 1
# while exponent != 0:
#     result = result * base
#     exponent -= 1
#
# print ("the computer value is", result)

#Solution 2 Using For Loop
# base = int(input("enter a base number here: "))
# exponent = int(input("enter exponent here: "))
#
# result = 1
#
# for i in range (exponent,0,-1):
#     result = result*base
#
# print ("the computed value is", result)

#Solution 3 Using power() function

# base = 4
# exponent = 3
#
# x = pow(base, exponent)
#
# print ("the computed value is", x)

#Solution 4 Using Exponentiation Operator

base = 4
exponent = 3

x = base ** exponent
print (x)


