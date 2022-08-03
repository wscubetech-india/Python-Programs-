# #Solution 1 Using ANSI Escape Sequences
#
# print ('\x1b[33m' + 'WsCubeTech' + '\x1b[35m')


from colorama import Fore, Back

print (Fore.LIGHTMAGENTA_EX,"Hello world")













#Solution 2 Using termcolor module