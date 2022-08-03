lower = int(input("enter lower limit here (>1) : "))
upper = int(input("enter upper limit here: "))

for i in range (lower, upper+1):
    if i > 1:
        for num in range (2,i):
            if i%num== 0:
                break
        else:
            print (i)