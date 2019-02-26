#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Don't expect a markup language (En serio, no lo es.)
html = open("test.html","w")
open = open("test.deml","r")
#tag_dictionary
tag_dictionary=["html{","head{","body{","a{","div{",
"h1{","h2{","h3{","h4{","h5{","h6{","li{","ol{","ul{","p{","span{"]
tag_transformA=["<html>","<head>","<body>","<a>","<div>","<h1>","<h2>",
"<h3>","<h4>","<h5>","<h6>","<li>","<ol>","<ul>","<p>","<span>"]
#special_dictionary
special_dictionary=[]
#GLOBALS:
global close
global tag
#Stacks
GeneralStack = []
OrderStack = []
PreStack = []
PostStack = []
def Stacking():
    for line in open:
        GeneralStack.append(line.strip())
    for stack in GeneralStack:
        if stack in tag_dictionary:
            PreStack.append("<"+stack.replace("{","")+">")
        elif "}" in stack:
            PreStack.append(stack)
        else:
            PreStack.append(stack)
#VERIFY TAGS IN PRESTACK BY USING DICTIONARY
'''
def Tag():
    for x in PreStack:
        if x in tag_transformA:
            return True
        else:
           return False
'''

Stacking()


for i in range(0, len(PreStack)-1):
        if PreStack[i+1] in tag_transformA:
            PostStack.append(PreStack[i].replace("<","</"))
        elif PreStack[i] in tag_transformA:
            OrderStack.append(PreStack[i].replace("<","</"))
#REPEAT LOOPS NEED IMPROVEMENT
for x in PostStack:
    if "}" in PostStack:
        PostStack.remove("}")

for y in PostStack:
    if "}" in PostStack:
        PostStack.remove("}")

PostStack.reverse()#OTRA ÑAPA
for z in range(0, len(PostStack)):

    OrderStack.append(PostStack[z])
count=0

for w in range(0,len(PreStack)):
    if "}" in PreStack[w]:
        count+=1
        PreStack[w] = OrderStack[count-1]

print(PreStack)
for xyz in PreStack:
    print(xyz)
    html.write(xyz+"\n")
