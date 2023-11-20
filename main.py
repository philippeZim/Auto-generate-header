import sys

fileToGen = sys.argv
directFile = ""
if len(fileToGen) > 1 and not directFile:
    directFile = str(fileToGen[1])
# read lines of file
fs = []
with open(directFile, "r") as f:
    fs = f.read().splitlines()

# get all includes
cur = 0
includes = []
while "class" not in fs[cur]:
    if "include" in fs[cur]:
        includes.append(fs[cur])
    cur += 1

# get the class name
classStr = fs[cur]
className = classStr[classStr.find("class") + 5: classStr.find("{")].strip()
cur += 1

# get the class body and extract functions
classBody = []
funs = []

while cur < len(fs):
    if not fs[cur].strip():
        cur += 1
        continue
    if "{" in fs[cur]:
        classBody.append(fs[cur][:fs[cur].find(")") + 1] + ";")
        opens = 0
        fn = []
        frs = True
        while opens > 0 or frs:
            frs = False
            fn.append(fs[cur])
            if "{" in fs[cur]:
                opens += 1
            if "}" in fs[cur]:
                opens -= 1
            if opens != 0:
                cur += 1
        funs.append(fn)
    else:
        classBody.append(fs[cur])
    cur += 1

# build the header file

hl = []

line1 = "#ifndef " + className.upper() + "_H"

line2 = "#define " + className.upper() + "_H"

hl.append(line1)
hl.append(line2)
hl.append("")

for x in includes:
    hl.append(x)
hl.append("")

hl.append(classStr)

for x in classBody:
    hl.append(x)
hl.append("")

hl.append("#endif")

# build the cpp file

cl = []

cl.append("#include \"" + className + ".h\"")
cl.append("")
"""
void test(int sj) {
void Port::test(int sj) {
"""


def addClassToFun(input):
    w = input.split()
    for i in range(len(w)):
        if "(" in w[i]:
            if w[i].find("(") == 0:
                w[i - 1] = className + "::" + w[i - 1]
            else:
                w[i] = className + "::" + w[i]

    return " ".join(w)


for x in funs:
    el1 = addClassToFun(x[0])
    cl.append(el1)
    for i in range(1, len(x)):
        cl.append(x[i][8:])
    cl.append("")

# ToDo Save className.cpp and className.h files
cppFile = "\n".join(cl)
hFile = "\n".join(hl)

with open(className + ".cpp", "w") as f:
    f.write(cppFile)
    f.close()

with open(className + ".h", "w") as f:
    f.write(hFile)
    f.close()