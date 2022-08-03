#Solution 1 Using os Module
# import os
#
# print (os.path.abspath(os.getcwd()))
# print (os.path.dirname(os.path.abspath("C:/Users/wscub/Desktop/YT mini programs/accessListIndex.py")))

#Solution 2 Using pathlib Module

import pathlib

print (pathlib.Path().absolute())
print (pathlib.Path("C:/Users/wscub/Desktop/Pandas Programs/file1.csv").parent.absolute())







