#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#TESTING VERSION
from dictionarytest import *
from stacktest import *

html = open("test.html","w")
deml = open("testing.deml","r")

stack = Stack();

for lines in deml:
    Stack_A.append(lines)

def ToStackB(what):
    Stack_B.append(what)

def WhatisEachElement():
    for i in Stack_A:
        if i.replace("{\n", "") in Simple_dictionary:
            ToStackB("<"+i.replace("{\n","")+">")
            print(Stack_B)
            print("etiqueta simple: " + i)
        else:
            if i == "}\n":
                print("Cierre: " + i)
            else:
                print("Texto o etiqueta compleja: "+  i)



WhatisEachElement()
print(Stack_B)
