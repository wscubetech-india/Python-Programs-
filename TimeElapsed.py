#Solution 1 Using Time Module
# import time
# starting_time = time.time()
#
# num = int(input("enter a number here: "))
# num1 = int(input("enter a number here: "))
# print (num+num1)
#
# ending_time = time.time()
#
# print (ending_time - starting_time)

#Solution 2 Using Timeit Module

from timeit import default_timer as timer

starting_time = timer()

num = int(input("enter a number here: "))
num1 = int(input("enter a number here: "))
print (num+num1)

ending_time = timer()

print (ending_time - starting_time)


