#Solution 1 Using | Operator

# a = {"John":38,"Lisa":44}
# b = {"Lisa":47,"Peter":40}
#
# print ( a | b)

# Solution 2 Using ** Operator
#
# a = {"John":38,"Lisa":44}
# b = {"Lisa":47,"Peter":40}
#
# print ({**a, **b})

#Solution 3 using copy() and update() methods

a = {"John":38,"Lisa":44}
b = {"Lisa":47,"Peter":40}


c = b.copy()
c.update(a)

print (c)












