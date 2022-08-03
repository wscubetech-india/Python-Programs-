#Solution 1 using Glob Module and os Module

# import glob, os
#
# os.chdir("C:/Users/wscub/Desktop/YT mini programs")
#
# for files in glob.glob("*.txt"):
#     print(files)

#Solution 2 Using os Module
# import os
#
# for files in os.listdir("C:/Users/wscub/Desktop/YT mini programs"):
#     if files.endswith(".txt"):
#         print (files)

#Solution 3 Using os.walk()
import os

for root,dir,files in os.walk("C:/Users/wscub/Desktop/YT mini programs"):
    for file in files:
        if file.endswith(".txt"):
            print (file)

