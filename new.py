#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Don't expect a markup language (En serio, no lo es.)
html = open("test.html", "w")#THIS GOES FIRST BC POTATO
open = open("test.deml", "r")


#testing tags
tag_dictionary=["html","head","body","a","div","h1","h2","h3","h4","h5","h6","li","ol","ul","p","span"]
#testing tags
special_dictionary=[]

tag_transformA=["<html>","<head>","<body>","<a>","<div>","<h1>","<h2>",
"<h3>","<h4>","<h5>","<h6>","<li>","<ol>","<ul>","<p>","<span>"]
tag_transformB=["</html>","</head>","</body>","</a>","</div>","</h1>","</h2>",
"</h3>","</h4>","</h5>","</h6>","</li>","</ol>","</ul>","</p>","</span>"]

global close

stackA=[]
stackB=[]

GeneralStack = []
OrderStack = []

count=0
newline = ""

def isolate(line):
    linecheck = line.replace("{","")
    newline = linecheck.strip()
    if newline in tag_dictionary:
        return True
    else:
        return False

def AddtoStack():

    for line in open:
        GeneralStack.append(line)
        if isolate(line):
            print(line.strip() + " [Added to Stacker]")
            stackA.append(line)
        if not isolate(line):
            print(line.strip() + " [Not added to Stacker (NOT A TAG)]")
            stackB.append(line)

def Clean():
    for order in range(len(GeneralStack)):
        S1 = GeneralStack[order].replace("{","")
        Cstack = S1.strip()
        if Cstack in tag_dictionary:
            OrderStack.append("<"+ Cstack + ">")
            close = "</" + Cstack + ">"
        elif Cstack is "}":
            OrderStack.append(Cstack + " " + close)

        else:
            OrderStack.append(Cstack)



AddtoStack()
Clean()
OrderStack.insert(len(GeneralStack),"<h2 style='color:orange'>POWERED BY DEML(Don't Expect a Markup Language)</h2>")
print("\n\nORDER STACK ELEMENTS: " + str(OrderStack))

for lines in OrderStack:
    print(lines)
    html.write(lines)




stackALen = len(stackA)
stackBLen = len(stackB)
print("\n\n"+str(stackALen) + " stackA")
print(str(stackBLen) + " stackB")
print("\n\nStackerA content: " + str(stackA))
print("\n\nStackerB content: " + str(stackB))
print("\n\nGeneral Stacker content: " + str(GeneralStack))
