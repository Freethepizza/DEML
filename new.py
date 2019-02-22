#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Don't expect a markup language (En serio, no lo es.)
open = open("test.deml", "r")


#testing tags
tag_dictionary=["html","head","body","a","div","h1","h2","h3","h4","h5","h6","li","ol","ul","p","span"]
#testing tags
special_dictionary=[]

tag_transformA=["<html>","<head>","<body>","<a>","<div>","<h1>","<h2>",
"<h3>","<h4>","<h5>","<h6>","<li>","<ol>","<ul>","<p>","<span>"]
tag_transformB=["</html>","</head>","</body>","</a>","</div>","</h1>","</h2>",
"</h3>","</h4>","</h5>","</h6>","</li>","</ol>","</ul>","</p>","</span>"]

stackA=[]
stackB=[]

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
        if isolate(line):
            print(line.strip() + " [Added to Stacker]")
            stackA.append(line)
        if not isolate(line):
            print(line.strip() + " [Not added to Stacker (NOT A TAG)]")

AddtoStack()
print("\n\nStackerA content: " + str(stackA))
