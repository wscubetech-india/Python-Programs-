friends = {"Rachel":"Ross","Monica":"Chandler","Phoebe":"Joe"}
print (friends)
# print (friends["Rachel"])

#solution 1 with .items
# for key,value in friends.items():
#     print (key,value)

#solution 2 with keys
# for i in friends.keys():
#     print (i, friends[i])

#solution 3 with keys and values
for i in friends.keys():
    print (i)

for values in friends.values():
    print (values)

