#Solution 1 Using Dictionary

# string = "Harry Potter and the Prisoner of Azkaban"
# vowels = "aeiou"
# string = string.casefold()
# # print (string)
#
# count = {}.fromkeys(vowels,0)
# # print (count)
# for char in string:
#     if char in count:
#         count[char]+=1
#
# print (count)

#Solution 2 Using List and Dictionary Comprehension

string = "Harry Potter and the Prisoner of Azkaban"
vowels = "aeiou"
string = string.casefold()

count = {key:sum([1 for char in string if char == key]) for key in vowels}

print (count)







