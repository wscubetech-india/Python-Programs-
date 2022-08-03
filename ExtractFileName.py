#Solution 1 Using os Module

# import os
#
# ext_name = os.path.basename("C:/Users/wscub/Desktop/YT mini programs/file.txt")
# print (ext_name)

#Solution 2 Using Path Module

from pathlib import Path

print(Path("C:/Users/wscub/Desktop/YT mini programs/file.txt").stem)







