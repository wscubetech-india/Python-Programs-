num = input("enter something here: ")

def check_float(num):
    try:
        float(num)
        return True
    except:
        return False

print (check_float(num))