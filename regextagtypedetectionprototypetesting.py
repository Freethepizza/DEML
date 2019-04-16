#REGEX BASED DEML TAG TYPE DETECTION
import re


deml = open("test.deml")
#PATTERNS:
#h1-h6
hx = re.compile('[a-zA-Z][1-6]\{|[a-zA-Z][1-6]\s\{|[a-zA-Z][1-6]\n\{')
#tag with class
tclass = re.compile('[a-zA-Z]+[.]+.*\{|[a-zA-Z]+[.]+.*\s\{|[a-zA-Z]+[.]+.*\n\{')
#tag with id
tid = re.compile('[a-zA-Z]+[#]+.*\{|[a-zA-Z]+[#]+.*\s\{|[a-zA-Z]+[#]+.*\n\{')
#simple tag
st = re.compile('\w+[a-zA-Z]\{|[a-zA-Z]\s\{|[a-zA-Z]\n\{')
'''
word0 = "span{"
word = "h6{"
word2 = "h1 {"
word3 = "h1\n{"
xx = re.match(st,word0)
print(xx)
print(bool(xx))
x = re.match(hx, word)
print(x)
print(bool(x))
y = re.match(hx, word2)
print(y)
print(bool(y))
z = re.match(hx, word3)
print(z)
print(bool(z))

word4 = "div.clase,clase{"
w = re.match(tclass, word4)
print(w)
print(bool(w))

word6 = "div#id,id{"+
v = re.match(tid, word6)
print(v)
print(bool(v))

if bool(w) is True:
    newword4 = word4.replace("{","")
    trozos = newword4.split('.')
    print(trozos)
    print("<"+trozos[0]+ " class='"+trozos[1].replace(","," ") + "'>")
else:
    print("no match")
'''
def clean(what):
    return what.replace("{\n","")

stackA = []

#Tag diferenciation process
for lines in deml:
    i = re.match(tclass,lines)
    u = re.match(tid,lines)
    e = re.match(st,lines)
    print(lines)
    if bool(i) is True:
        print(lines + "    TAG WITH CLASS!")
        new = clean(lines)
        print(new)
        newseparated = new.split(".")
        classes = newseparated[1].replace(","," ")
        finalclasstag = "<" + newseparated[0] + " class='"+classes.replace("\n","")+"'>"
        print(finalclasstag)
        stackA.append(finalclasstag)
    elif bool(u) is True:
        print(lines+ "     TAG WITH ID!")
        new = clean(lines)
        newseparated = new.split("#")
        ids = newseparated[1].replace(","," ")
        finalidtag =  "<" + newseparated[0] + " id='"+ids.replace("\n","")+"'>"
        stackA.append(finalidtag)
    elif bool(e) is True:
        print(lines + "    SIMPLE TAG!")
        new = clean(lines)
        finaltag = "<"+ new +">"
        stackA.append(finaltag)


print(stackA)

for elements in stackA:
    print(elements + "\n")
