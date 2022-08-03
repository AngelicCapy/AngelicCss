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

keyword = [".","#","if","elif","else:","end","=","for","while","do","end","return","break","continue","pass","import","from","as","global","nonlocal","assert","del","raise","try","except","finally","with","yield","lambda","and","or","not","in","is","is not","for","in","not","not in","if","elif","else:","end","=","for","while","do","end","return","break","continue","pass","import","from","as","global","nonlocal","assert","del","raise","try","except","finally","with","yield","lambda","and","or","not","in","is","is not","for","in","not","not in","if","elif","else:","end","=","for","while","do","end","return","break","continue","pass","import","from","as","global","nonlocal","assert","del","raise","try","except","finally","with","yield","lambda","and","or","not","in","is","is not","for","in","not","not in","if","elif","else:","end","=","for","while","do","end","return","break","continue","pass","import","from","as","global","nonlocal","assert","del","raise","try","except","finally","with","yield","lambda","and","or","not","in","is","is not","for","in","not","not in","if","elif","else:","end","=","for","while","do","end","return","break","continue","pass","import","from","as","global","nonlocal","assert","del","raise","try","except","finally","with","yield","lambda","and","or","not","in","is","is not","for","in","not","not in","if","elif","else:","end","=","for","while","do","end","return","break","continue","pass","import","from","as","global","nonlocal","assert","del","raise","try","except","finally","with","yield","lambda","and","or","not","in","is","is not","for","in","not","not in","if","elif","else:","end","=","for","while","do","end","return","break","continue","pass",""]

def modification(line):
    #<==Space Detection==>
    size = 0
    if len(line) >= 2: 
        if "    " in line[1]:
            size = len(line[1]) // 4
        line = "".join(line).split()
    #<==Variable Case==>
    if "=" in line: #a = "Hello World" -> $a: "Hello World";
        line[0] = "$"+line[0] + ":"
        line[1] = "".join(line[2:]) +";"
        line = line[0:2]
    #<==Keyword Case==>
    for i in line:
        if i not in keyword and i[0] !="$" and i[0] != '"' and i[0] != "'" and i[0].isdigit() == False and not "false" in i and not "true" in i and i[0]!="#" and i[0]!=".":
            line = line[:line.index(i)] + ["$"+i] + line[line.index(i)+1:]
            break
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
        line[3] = line[3].split("..")
        line = ["@for " + line[1] + " from " + line[3][0] + " through " + line[3][1][0:-1] + " {" ]





    # In Coming Soon

    #while
    #object
    #use
    #import 
    #Mixin
    #Includes
    #Extends
    #each
    #Class
    #Id
    #Function
    

    # End





    #<==Intedention Application==>
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
        sleep(1)


#<============================================================================>





#<============================================================================>
#<===========================>Boucle Principale<==============================>
#<============================================================================>

while True: # Redo main in infinite
    main()

#<============================================================================>