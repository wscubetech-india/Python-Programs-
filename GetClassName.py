#Solution 1 using __class__.__name__

class SmartPhone:
    def name(self,name):
        return name

s1 = SmartPhone()
print (s1.__class__.__name__)

#Solution 2 using type() and __name__attributes
#
# class SmartPhone:
#     def name(self,name):
#         return name
#
# s1 = SmartPhone()
# print (type(s1).__name__)


