#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Don't expect a markup language (En serio, no lo es.)

#Imports:
from dictionary import *
from stacker import *
from error import *
#html = open("test.html","w")
deml = open("test.deml","r")

def Line_Parsing():
    for line in deml:
        Parsed_tag = line.split("{")
        if Parsed_tag[0] in Simple_dictionary:
            To_Stack_A(Parsed_tag[0])
            To_GeneralStack(Parsed_tag[0])

        elif "}" in line.replace(" ",""):
            print("Close: Will be added to Stack_C")
            To_Stack_C(line.replace(" ",""))
            To_GeneralStack(line.replace(" ",""))
        else:
            print("Plain Text: Will be added to Stack_B")
            To_Stack_B(line)
            To_GeneralStack(line)

def Tag_Trasform(stack):
    for index in range(0, len(stack)):
        stack[index] = "<" + stack[index] + ">"


def HTML_Precompilation():
    count=-1
    for element in GeneralStack:
        count+=1
        if element in Stack_A:
            print("Open INDEX: "+str(count))
        elif "}" in element:
            print("\tClose INDEX: "+str(count))


Line_Parsing()
HTML_Precompilation()


print("\n-----------TESTS-------------------------------------------")
print("|Stack_A: "+ str(Stack_A))
print("|Stack_B: "+ str(Stack_B))
print("|Stack_C: "+ str(Stack_C))
print("|GeneralStack: "+ str(GeneralStack))


CheckIntegrity_A()
