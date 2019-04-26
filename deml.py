#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Don't expect a markup language (En serio, no lo es.)
from i_o import *
from stack import *
from dparse import *

for lines in deml:
    ToStack_A(lines)
    tagtype(lines)
    toRNA(lines)

for i in range(0,len(Stack_A)):
    if tagtype(Stack_A[i]) is 0:
        type = 0
        Stack_A[i] = Stack_A[i].split(".")
        Stack_A[i][1] = Stack_A[i][1].replace("{","")
        Stack_A[i][1] = Stack_A[i][1].replace("\n","")
        Stack_A[i][1] = 'class="'+Stack_A[i][1].replace(","," ")+'"'
    elif tagtype(Stack_A[i]) is 1:
        Stack_A[i] = Stack_A[i].split("#")
        Stack_A[i][1] = Stack_A[i][1].replace("{","")
        Stack_A[i][1] = Stack_A[i][1].replace("\n","")
        Stack_A[i][1] = 'id="'+Stack_A[i][1].replace(","," ")+'"'
    elif tagtype(Stack_A[i]) is 2:
        Stack_A[i] = Stack_A[i].replace("{","")
        Stack_A[i] = Stack_A[i].replace("\n","")


print(Stack_A)

print(RNA)
