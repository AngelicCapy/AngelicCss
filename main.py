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

def modification(line):
    #<==Space Detection==>
    Space = False
    if line[1] == "    ":
        Space = True
    line = "".join(line).split()
    


    #<==Variable Case==>
    if "=" in line: #a = "Hello World" -> $a: "Hello World";
        if Space:
            line[0] = "    " + "$"+line[0] + ":"
        else:
            line[0] = "$"+line[0] + ":"
        line[1] = " ".join(line[2:]) +";"+"\n"
        line = line[0:2]
        


    #<==IF-ELSEIF-ELSE==>
    if len(line) >= 2 and line[0] == "if":
        line[0] = "@if(" + "".join(line[1:]).replace(":","") + ") {"
        line[1:] = []



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