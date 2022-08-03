#Solution 1 Using readlines()

# f = open("file.txt","r")
# line = f.readlines()
# print (line)
#
# new_lines = [x.strip() for x in line]
# print (new_lines)


#Solution 2 Using For Loop and List comprehension
f = open("file.txt","r")
lines = [line for line in f]
print (lines)
new_lines = [x.strip() for x in lines]
print (new_lines)



