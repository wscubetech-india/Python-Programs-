l = [2,5,7,3,6,8,3,2,1,6,9]
# def even_odd(num):
#     if num%2==0:
#         return True
#     else:
#         return False

even_nums = filter(lambda x : x%2==0,l)

for i in even_nums:
    print (i)
