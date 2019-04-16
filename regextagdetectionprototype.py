#REGEX BASED DEML TAG TYPE DETECTION
import re

#PATTERNS:
#h1-h6
hx = re.compile('[a-zA-Z][1-6]\{|[a-zA-Z][1-6]\s\{|[a-zA-Z][1-6]\n\{')
#tag with class
tclass = re.compile('[a-zA-Z]+[.]+.*\{|[a-zA-Z]+[.]+.*\s\{|[a-zA-Z]+[.]+.*\n\{')
#tag with id
tid = re.compile('[a-zA-Z]+[#]+.*\{|[a-zA-Z]+[#]+.*\s\{|[a-zA-Z]+[#]+.*\n\{')

word = "h6{"
word2 = "h1 {"
word3 = "h1\n{"
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

word6 = "div#id,id{"
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
