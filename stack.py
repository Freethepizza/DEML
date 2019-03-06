#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Stack
from dictionary import *
Stack_A = []
def ToStack_A(what):
    Stack_A.append(what)
def CleanStack(stack):
    for i in range(0, len(stack)):
        if stack[i].replace("{\n","") in Simple_dictionary:
            stack[i] = stack[i].replace("{\n","")
        elif "}" in stack[i].replace("\n",""):
            stack[i] = stack[i].replace("\n","")
RNA=[]
DNA=[]
Final=[]
def ToDNA(what):
    DNA.append(what)
def ToRNA(what):
    RNA.append(what)

def Translation(what):
    for elem in what:
        if elem in Simple_dictionary:
            ToRNA(elem)
            ToDNA("(")
        elif "}"==elem:
            ToRNA(")")
            ToDNA(")")
        else:
            ToRNA("T")
            ToDNA("#")

def ToString(what):
    return "".join(what)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def last_item(self):
        return self.items[-1]

    def print_stack(self):
        print(self.items)

stack = Stack()