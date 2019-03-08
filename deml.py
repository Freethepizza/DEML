#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Don't expect a markup language (En serio, no lo es.)
from stack import *
from i_o import *
from parser_ import *



print(Stack_A)
print(RNA)
print(DNA)
print(ToString(RNA))
print(ToString(DNA))

print(RNA)
'''
stack.push("head")
stack.print_stack()
stack.pop()
stack.print_stack()
stack.push("body")
stack.print_stack()
stack.push("div")
stack.print_stack()
stack.push("h1")
stack.print_stack()
stack.pop()
stack.print_stack()
stack.push("p")
stack.print_stack()
stack.pop()
stack.print_stack()
stack.pop()
stack.print_stack()
stack.push("span")
stack.print_stack()
stack.pop()
stack.print_stack()
stack.pop()
stack.print_stack()
'''
stack.print_stack()
for lines in RNA:
    html.write(lines)

Compile()
