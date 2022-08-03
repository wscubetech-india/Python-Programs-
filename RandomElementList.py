#Solution 1 Using Random Module

# import random
# l = ["a",1,5,"b","o",7]
#
# random_value = random.choice(l)
# print (random_value)

#Solution 2 using Secret Module

import secrets
l = ["a",1,5,"b","o",7]
random_value = secrets.choice(l)
print (random_value)


