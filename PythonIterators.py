class Fantastic_Five:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            value = self.num
            self.num+=1
            return value
        else:
            raise StopIteration

FF = Fantastic_Five()

for i in FF:
    print (i)














# string = "WsCube Tech"
# iterate = iter(string)
#
# print (iterate.__next__())
# print (next(iterate))
# print (next(iterate))



# for i in string:
#     print (i)



# nums = [1,2,3,4,5,6]
#
# iterate = iter(nums)
# print (iterate.__next__())
# print (iterate.__next__())
# print (iterate.__next__())
# for i in nums:
#     print (i)