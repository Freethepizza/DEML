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
        stack.push(Stack_A[i][0])
        Stack_A[i][1] = Stack_A[i][1].replace("\n","")
        Stack_A[i] = "<" + Stack_A[i][0] + ' id="'+Stack_A[i][1].replace(","," ")+'">'
        html.write(Stack_A[i])
    elif tagtype(Stack_A[i]) is 1:
        Stack_A[i] = Stack_A[i].split("#")
        stack.push(Stack_A[i][0])
        Stack_A[i][1] = Stack_A[i][1].replace("{","")
        Stack_A[i][1] = Stack_A[i][1].replace("\n","")
        Stack_A[i] = "<" + Stack_A[i][0] + ' id="'+Stack_A[i][1].replace(","," ")+'">'
        html.write(Stack_A[i])
    elif tagtype(Stack_A[i]) is 2:
        stack.push(Stack_A[i])
        Stack_A[i] = Stack_A[i].replace("{","")
        Stack_A[i] = Stack_A[i].replace("\n","")
        Stack_A[i] = "<"+Stack_A[i]+">"
        html.write(Stack_A[i])
    elif tagtype(Stack_A[i]) is 3:
        Stack_A[i] = "</"+ stack.last_item().replace("{\n","")+">"
        stack.pop()
        html.write(Stack_A[i])
    else:
        html.write(Stack_A[i])

    stack.print_stack()

print("".join(Stack_A))


print(RNA)
