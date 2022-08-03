# #Solution 1 Using For Loop
# lower = int(input("enter lower limit here: "))
# upper = int(input("enter upper limit here: "))
#
# for i in range (lower,upper+1):
#     if i % 13 == 0:
#         print (i)

#Solution 2 Using Lambda Function and filter()

l = [39,78,65,34,103,130,50,70]

result = list(filter(lambda x : x % 13== 0,l))

print ("The values that are divisible by 13 are",result)
