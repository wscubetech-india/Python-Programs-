#Solution 1 Using os Module
# import os
#
# file_size = os.stat("C:/Users/wscub/Desktop/YT mini programs/AddTwoMatrices.py")
# print (file_size.st_size)

#Solution 2 Using Pathlib Module
from pathlib import Path

file_size = Path("C:/Users/wscub/Desktop/YT mini programs/AddTwoMatrices.py")
print (file_size.stat().st_size)