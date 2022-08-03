#Solution 1 Using + Operator
# l1 = [3,6,8,2,"a","j"]
# l2 = [3,6,"k","f","j"]
#
# l3 = l1+l2
# print (l3)

#Solution 2 with Unique Values

# l1 = [3,6,8,2,"a","j"]
# l2 = [3,6,"k","f","j"]
#
# l3 = list(set(l1+l2))
# print (l3)

#Solution 3 Using extend() function
l1 = [3,6,8,2,"a","j"]
l2 = [3,6,"k","f","j"]

l2.extend(l1)
print (l2)







