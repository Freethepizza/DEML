#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#Parser
from stack import *
from i_o import *
for lines in deml:
    ToStack_A(lines)
CleanStack(Stack_A)
Translation(Stack_A)
iterator = iter(RNA)

def Compile():
    nextpos=0
    for i in ToString(DNA):
        nextpos+=1
        pos= nextpos-1
        if i=="(":
            stack.push(RNA[pos].replace("<","\n</"))
            #stack.print_stack()
        elif  i==")":
            RNA[pos]=stack.last_item()
            stack.pop()
            #stack.print_stack()
