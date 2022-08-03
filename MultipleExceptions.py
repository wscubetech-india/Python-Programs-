string = input("enter something here: ")
try:
    num = int(input("enter a number here: "))

    print (string + num)
except (ValueError,TypeError) as a:
    print (a)

print ("thank you")

