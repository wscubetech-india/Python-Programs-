def pos_neg(num):
    if num>0:
        return "{} is a positive number".format(num)
    else:
        return "{} is a negative number".format(num)

l = [1,-6,3,9,-10,-16,4,19,-2]

pn = (list(map(pos_neg,l)))

for i in pn:
    print (i)


# for i in l:
#     if i >0:
#         print (i, "is pos")
#     else:
#         print (i, "is neg")
# print (pos_neg(-24))