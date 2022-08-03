from enum import Enum

class Smartphones(Enum):
    Samsung = 1
    Nokia = 2
    Apple = 3

print (Smartphones.Samsung)
print (Smartphones.Samsung.name)
print (Smartphones.Samsung.value)
