#!/usr/bin/python
import os
PATH=input("PATH to data: ")
files=os.listdir(PATH)
[os.replace(file,file.replace(" ","_")) for file in files]
