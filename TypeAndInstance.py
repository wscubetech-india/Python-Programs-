class SmartPhone:
    def name(self):
        pass

class Nokia(SmartPhone):
    def phone_name(self):
        pass

obj_SP = SmartPhone()
obj_N = Nokia()

print ("for type() function")
print (type(obj_SP) == SmartPhone)
print (type(obj_N) == SmartPhone)

print ()
print ("for isinstance")
print (isinstance(obj_SP,SmartPhone))
print (isinstance(obj_N,SmartPhone))


