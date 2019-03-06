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


def Compile():
    for i in range(0, len(RNA)):
        if RNA[i] in Simple_dictionary:
            stack.push("<"+RNA[i]+">")
            RNA[i] = "<"+RNA[i]+">"
        elif RNA[i] == "#":
            continue
        elif RNA[i] == ")":
            newtag = str(stack.last_item()).replace("<","</")
            stack.pop()
            RNA[i] = newtag
