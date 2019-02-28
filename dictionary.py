#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Nesting
from nesting import *
#PRE
Simple_dictionary = ["html","head","body","footer","a","div","h1","h2","h3","h4",
"h5","h6","li","ol","ul","p","span","b","i"]
Complex_dictionary = []
Special_dictionary = []

#POST
Stack_A = []
Stack_B = []
Stack_C = []
GeneralStack = []
NestingStack = []
ControlStack = []
FinalStack = []

def To_Nesting():
    for level in GeneralStack:
        if level in Level_0:
            print("Level_0: " + level)
            NestingStack.append("L0")
        elif level in Level_1:
            print("Level_1: " + level)
            NestingStack.append("L1")
        elif level in Level_2:
            print("Level_2: " + level)
            NestingStack.append("L2")
        elif level in Level_X:
            print("Level_X: " + level)
            NestingStack.append("LX")
        elif "}" in level.strip():
            NestingStack.append("125")
        else:
            NestingStack.append("FF")
