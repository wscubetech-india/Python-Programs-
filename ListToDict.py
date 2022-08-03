#Solution 1 Using zip() and Dictionary Methods:

# name = ["John", "Peter","Lisa","David"]
# marks = [98,78,88,72]
#
# dictionary = zip(name,marks)
# print (dict(dictionary))

#Solution 2 Using zip() and List Comprehension
name = ["John", "Peter","Lisa","David"]
marks = [98,78,88,72]

dictionary = {key:value for key, value in zip(marks,name)}
print (dictionary)











