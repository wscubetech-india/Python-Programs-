nterms = int(input('enter a number here: '))

power = list(map(lambda x : 2 ** x,range(nterms+1)))

# print (power)

for i in range (nterms+1):
    print ("the value of 2 raised to the power",i,"is",power[i])