#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Dictionary + parser
import re
from i_o import deml
from stack import *
#PATTERNS
#tag with class
tclass = re.compile('[a-zA-Z1-6]+[.]+.*\{|[a-zA-Z1-6]+[.]+.*\s\{|[a-zA-Z1-6]+[.]+.*\n\{')
#tag with id
tid = re.compile('[a-zA-Z1-6]+[#]+.*\{|[a-zA-Z1-6]+[#]+.*\s\{|[a-zA-Z1-6]+[#]+.*\n\{')
#simple tag
st = re.compile('\w+[a-zA-Z1-6]\{|[a-zA-Z1-6]\s\{|[a-zA-Z1-6]\n\{')
#cierre
close = re.compile('[}]')

RNA = []

Stack_A = []

def tagtype(tag):
    classtag = re.match(tclass,tag)
    idtag = re.match(tid,tag)
    simpletag = re.match(st,tag)
    closing = re.match(close,tag)
    if bool(classtag) is True:
        return 0
    elif bool(idtag) is True:
        return 1
    elif bool(simpletag) is True:
        return 2
    elif bool(closing) is True:
        return 3
    else:
        return 4;

def ToStack_A(tag):
    Stack_A.append(tag)

def toRNA(tag):
    if tagtype(tag) is 0:
        RNA.append("(")
    elif tagtype(tag) is 1:
        RNA.append("(")
    elif tagtype(tag) is 2:
        RNA.append("(")
    elif tagtype(tag) is 3:
        RNA.append(")")
    else:
        print("text")
        RNA.append("%")

def Tagtranslation(tag):
    if tagtype(tag) is 0:
        tag.split(".")
