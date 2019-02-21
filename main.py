open = open("test.deml", "r")
#write = open("test.html", "w")
tags_=["html","head","body","a","b","div","h1","h2","h3","h4","h5","h6","li","ol","p","ul","span"]
cline = 0
count = 0
num=0
endings = []
code = []
moar = []
moar2 = []
full = []
for line in open:

    lineaux = line.rstrip()
    sline = line.split("{")
    cline+=1
    if "{" in lineaux:
        #print("Open: " + str(cline))
        print("<" + sline[0].strip() + ">" + str(cline))
        endings.append("<" + sline[0] + ">")
    if "}" in lineaux:
        print("Closed: " + str(cline))
        endings.append(str(cline))
    size = len(endings)
    code.append(line.strip())

print("\n\ntamaño o/c: " + str(size) + "\n\n")
print("BODY ARRAY:"+ str(endings))
print("RAW ARRAY: "+ str(code))
for tag in code:
    count+=1
    print(tag)
    if "}" in tag:
        moar.append(str(count) + " " + tag)
    if "{" in tag:
        moar2.append(str(count) + " " + tag)
    full.append(tag)
print(moar2)
print(moar)
print(full)

for x in full:
    num+=1
    if "}" in full[num-1]:
        print("</"+full[num-2]+">")
    else:
        print("<"+full[num-1]+">")
print(len(tags_))
print(tags_)
