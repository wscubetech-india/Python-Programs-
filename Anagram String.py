#Check Anagram

print ("program to check Anagram")
a1 = input("enter a word here: ")
a2 = input("enter another word here: ")

if len(a1) == len(a2):
    a1_sorted = sorted(a1)
    a2_sorted = sorted(a2)
    if a1_sorted == a2_sorted:
        print ("it is an anagram")
    else:
        print ("it is not an anagram")
else:
    print ('It is not an anagram')






