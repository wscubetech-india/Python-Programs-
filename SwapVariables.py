#Solution1 (Using third variable)
#
# a = 12
# b = 4
#
# temp = a
# print ("the value of a is",a)
# print ("the value of b is",b)
# # print ("the value of temp is",temp)
#
# a = b
# print ("the value of a after conversion is",a)
# b = temp
# print ("the value of b after conversion is",b)


#Solution2 (without using third variable)

a = 12
b = 4

a,b = b,a
print (a)
print (b)

