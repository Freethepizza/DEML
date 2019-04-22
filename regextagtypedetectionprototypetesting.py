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

StackA = []
StackB = []
StackC = []

def tagtype(tag):
    classtag = re.match(tclass,tag)
    idtag = re.match(tid, tag)
    simpletag = re.match(st, tag)

    if bool(classtag) is True:
        return 0
    elif bool(idtag) is True:
        return 1
    elif bool(simpletag) is True:
        return 2


def clean(tag):
    tag.replace("{","")
    if tagtype(tag) is 0:
        return tag.replace("{","")
    elif tagtype(tag) is 1:
        return tag.replace("{","")
    elif tagtype(tag) is 2:
        return tag.replace("{","")


def transform(tag):
    if tagtype(tag) is 0:
        newtag =  clean(tag).split(".")
        return "<" + newtag[0] + " class='"+ newtag[1].replace("\n", "") + "'>"
    elif tagtype(tag) is 1:
        newtag = clean(tag).split("#")
        return "<" + newtag[0] + " id='"+ newtag[1].replace("\n", "") + "'>"
    elif tagtype(tag) is 2:
        newtag = clean(tag)
        return "<" + newtag.replace("\n", "") + ">"

for lines in deml:
    clean(lines)
    StackA.append(transform(lines))

for lines in StackA:
    print(lines)
print(StackA)
