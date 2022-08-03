import os
from time import sleep

File = [i for i in os.listdir() if i.endswith(".acss") ]



def read_file(file):
    Acss = open(files, "r")
    Acss_content = Acss.read()
    Acss.close()
    return Acss_content

def write_file(file, content):
    Acss = open(file, "w")
    Acss.write(content)
    Acss.close()
    

while True:
    for files in File:
        content = read_file(files)
        write_file(files.replace("acss","css"), content)
    sleep(0.1)