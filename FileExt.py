#Solution 1 Using os Module

# import os
# file_ext = os.path.splitext("C:/Users/wscub/Desktop/YT mini programs/file.txt")
# print (file_ext[1])

#Solution 2 using Pathlib Module
from pathlib import Path

print (Path("C:/Users/wscub/Desktop/YT mini programs/file.txt").suffix)



