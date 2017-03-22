# Python version 2.7.13
# Author: Gavin Bramley
# Python Drill File Mover
# - Move the files from Folder A to Folder B.
# - Print out each file path that got moved onto the shell.
# - Upon viewing Folder A after the execution, the moved files should not be there.

import shutil
import os


path="C:/Miniconda3/pythondatetime/FolderA/"
moveto = "C:/Miniconda3/pythondatetime/FolderB/"
files = os.listdir(path)
files.sort()
for f in files:
    if f.endswith(".txt"):
        src= path+f
        dst = moveto+f
        shutil.move(src,dst)



