#<============================================================================>
#<============================>Module Importer<===============================>
#<============================================================================>
import os
import re
from time import sleep

#<============================================================================>




#<============================================================================>
#<===============================>Fonctions<==================================>
#<============================================================================>


def Read(files): # Files -> Each Line of the File
    Acss = open(files, "r")
    AcssContent = Acss.readlines()
    Acss.close()
    return AcssContent

def Write(files, AcssContent): # Each Line of the File -> Transformed Line -> Write in the CSS File
    Css = open(files.replace("acss","scss"), "w")
    for line in AcssContent:
        line = modification(re.split(r'(\s+)',line))
        Css.write(" ".join(line))
    Css.close()

#<============================================================================>




#<============================================================================>
#<================================>Syntaxe<===================================>
#<============================================================================>
Variable = []

def modification(line):
    #<==Space Detection==>
    size = 0
    if len(line) >= 2: 
        if "    " in line[1]:
            size = len(line[1]) // 4
        line = "".join(line).split()
    #<==Variable Case==>
    if "=" in line: #a = "Hello World" -> $a: "Hello World";
        if line[0] not in Variable:
            Variable.append(line[0])
        if line[2][0] != "[" and line[2][0] != "{": 
            line[0] = line[0] + ":"
            line[1] = "".join(line[2:]) +";"
            line = line[0:2]
        #<==Array==>
        elif line[2][0] == "[":

            line[0] = line[0] + ":"
            line[1] = ",".join(line[2].split(",")).replace("[","(").replace("]",")") +";"
            line = line[0:2]
        else:
            line[0] = line[0] + ":"
            line[1] = "".join(line[2:]).replace("=",":").replace("{","(").replace("}",")") +";"
            line = line[0:2]     
    #<==Keyword Case==>
    for i in Variable:
        for j in line: 
            if i in j and "'" not in j and '"' not in j:
                line[line.index(j)] = "$"+j
    #<==IF-ELIF-ELSE==>
    if len(line) >= 1 and line[0] == "if":
        line[0] = "@if (" + " ".join(line[1:]).replace(":","") + ") {"
        line[1:] = []
    if len(line) >= 1 and line[0] == "elif" :
        line[0] = "} @else if (" + " ".join(line[1:]).replace(":","") + ") {"
        line[1:] = []
    if len(line) >= 1 and line[0] == "else:":
        line = ["} @else {"]
    if line == ["end"]:
        line = ["}"]
    #<==For Loop==>
    if len(line) >= 1 and line[0] == "for":
        if len(line) <= 4:
            line[3] = line[3].split("..")
            line = ["@for " + "$"+line[1] + " from " + line[3][0] + " through " + line[3][1][0:-1] + " {" ]
        #<==Each==>
        else:
            line[2] = line[2].split(",")
            line[2] = ["$"+i for i in line[2]]
            line = ["@each " + ",".join(line[2]) + " in " + line[-1][:-1] + " {" ]
    #<==While==>
    if len(line) >= 1 and line[0] == "while":
        line[-1] = line[-1][:-1]
        line[0] = "@while (" + " ".join(line[1:]) + ") {"
        line[1:] = []
    #<==Function==>
    if len(line) >= 1 and line[0] == "def":
        line[-1] = line[-1][:-1]
        line[0] = "@function " 
        print(line)


    #<==Indentation Application==>
    line+=["\n"]
    line[0] = size*"    " + line[0]
    return line

#<============================================================================>



#<============================================================================>
#<==========================>Fonction Principale<=============================>
#<============================================================================>

def main(): # Locate every .acss -> Read the File -> Transform the Line -> Write the CSS File
    File = [i for i in os.listdir() if i.endswith(".acss") ]
    for files in File:
        AcssContent = Read(files)
        Write(files, AcssContent)
        sleep(10)


#<============================================================================>





#<============================================================================>
#<===========================>Boucle Principale<==============================>
#<============================================================================>

while True: # Redo main in infinite
    main()

#<============================================================================>