a = input("enter a sentence here: ")

l = a.split()
print (l)

for i in range (len(l)):
    l[i] = l[i].lower()
print (l)

l.sort()

for i in l:
    print (i)

