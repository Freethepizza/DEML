#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Stacker

from dictionary import Stack_A,Stack_B,Stack_C,GeneralStack,NestingStack,ControlStack,FinalStack
from error import *

close=[]

def To_Stack_A(tag):
    Stack_A.append(tag)
def To_Stack_B(tag):
    Stack_B.append(tag)
def To_Stack_C(tag):
    Stack_C.append(tag)
def To_GeneralStack(tag):
    GeneralStack.append(tag)

def To_FinalStack():
    if len(GeneralStack) is not  len(ControlStack):
        FinalStack_Error()
    else:
        for output in range(0, len(GeneralStack)):
            if "O" in ControlStack[output]:
                FinalStack.append("<"+GeneralStack[output]+">")
                close.append("</"+GeneralStack[output]+">")
            elif "T" in ControlStack[output]:
                FinalStack.append(GeneralStack[output])
            elif "C" in ControlStack[output]:
                FinalStack.append(close[output-output-1])
                print()
