import re, os, sys, glob, shutil

from tkinter import Tk
import tkinter as tk

from tkinter.filedialog import askdirectory
print("Select Folder where are the pdfs file of the research")
path_research_files = askdirectory(title='Select Folder where are the pdfs file of the research') # shows dialog box and return the path

print("Select drive where are the output drive and scripts")
path_txt0 = askdirectory(title='Select drive where are the output drive and scripts') # shows dialog box and return the path

with open('list_of_txt.txt') as fh:
        names = fh.read()
        #print(names)

os.chdir(path_txt0)
outfolder = "/out_txt/"
try:
    os.mkdir(outfolder)
except OSError:
    print ("Creation of the directory %s failed" % outfolder)
else:
    print ("Successfully created the directory %s " % outfolder)

print("Select Folder will be the output pdfs to be stored")
out = askdirectory(title='Select Folder will be the output pdfs to be stored') # shows dialog box and return the path

# Idea for the code from: https://stackoverflow.com/questions/18206918/python-search-and-copy-files-in-directory
os.chdir(path_research_files)
for root, dirs0, files0 in os.walk(path_research_files):
    for _file in files0:
        print(_file)
        if _file in names:
            #print(names)
            # If we find it, notify us about it and copy it it to C:\NewPath\
            #print(str(_file)+'Found file in: ' + str(root))
            shutil.copy(os.path.abspath(root + '/' + _file), out)
