import os
from time import sleep

File = [i for i in os.listdir() if i.endswith(".acss") ]


def modification(line):
    if line.startswith("ID:"):
        line = line.replace("ID:", "#")
    if line.startswith("CLASS:"):
        line = line.replace("CLASS:", ".")
    if line.startswith("TAG:"):
        line = line.replace("TAG:", "")
    if line.startswith("ATTRIBUTE:"):
        line = line.replace("ATTRIBUTE:", "")


    return line

for files in File:
    Acss = open(files, "r")
    Acss_content = Acss.readlines()
    print(Acss_content)
    Acss.close()
    Css = open(files.replace("acss","css"), "w")
    for line in Acss_content:
        line = modification(line)
        Css.write(line)
    Css.close()




"""
def read_file(file):
    Acss = open(files, "r")
    Acss_content = Acss.read()
    Acss.close()
    return Acss_content

def write_file(files, content):
    Acss = open(files, "w")
    Acss.write(content)
    Acss.close()
    




while True:
    for files in File:
        content = read_file(files)
        write_file(files.replace("acss","css"), content)
    sleep(0.1)
"""