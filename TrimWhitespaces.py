#Solution 1 Using strip() function

# string = "  \nI love Python  "
# print (string)
# print (string.strip(" "))

#Solution 2 Using Regular Expressions(RegEx)

import re

string = "   I love Python   "
x = re.sub(r'^\s+|\s+$','',string)
print (x)
