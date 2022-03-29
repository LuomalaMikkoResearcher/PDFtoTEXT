# Read: https://www.geeksforgeeks.org/how-to-install-anaconda-on-windows/
# Read: https://www.anaconda.com/distribution/#windows
# Install anacoda to pc (both path variables)
# Read: https://towardsdatascience.com/anaconda-start-here-for-data-science-in-python-475045a9627
# Read: https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/
# conda create -n tf-gpu tensorflow-gpu
# conda activate tf-gpu
# install in anacoda
# pip install tk
# pip install pdfminer


import os
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

from tkinter import Tk
import tkinter as tk

from tkinter.filedialog import askdirectory
print("Select folder where are the pdf files of datasets")
path_pdfs = askdirectory(title='Select folder where are the pdf files of dataset') # shows dialog box and return the path

os.chdir(path_pdfs)
# idea for the pdf to text file converter from: https://linuxtut.com/en/85ded85423be6108f05b/
pdf_folder_path = os.getcwd()			                #Get the path of the current folder
text_folder_path = os.getcwd() + '/' + 'text_folder'		#Notation of path is mac specification. For windows'/'To'\'Correct to.

os.makedirs(text_folder_path, exist_ok=True)
pdf_file_name = os.listdir(pdf_folder_path)

#name is a PDF file (ends.pdf) returns TRUE, otherwise FALSE is returned.
#This post was quoted and partially changed → http://qiita.com/korkewriya/items/72de38fc506ab37b4f2d
def pdf_checker(name):
	pdf_regex = re.compile(r'.+\.pdf')
	if pdf_regex.search(str(name)):
		return True
	else:
		return False

#Convert PDF to text file
def convert_pdf_to_txt(path, txtname, buf=True):
    rsrcmgr = PDFResourceManager()
    if buf:
        outfp = StringIO()
    else:
        outfp = file(txtname, 'w')
    #codec = 'utf-8'
    laparams = LAParams()
    laparams.detect_vertical = True
    device = TextConverter(rsrcmgr, outfp, laparams=laparams) # 20191010 version does not have the codec=codec option, so it is removed from code.
	# https://pypi.org/project/pdfminer/
	# https://pdfminersix.readthedocs.io/_/downloads/en/latest/pdf/
	# https://github.com/pdfminer/pdfminer.six/issues/232

    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()
    device.close()
    if buf:
        text = outfp.getvalue()
        make_new_text_file = open(text_folder_path + '/' + path + '.txt', 'w', encoding='utf-8') # koodia oli korjattua encoding='utf-8' jotta ei tule virhettä https://www.codegrepper.com/code-examples/python/UnicodeEncodeError%3A+%27charmap%27+codec+can%27t+encode+character+%27%5Cu2764%27+in+position+24925%3A
		# Idea for the code from: https://helperbyte.com/questions/476040/is-it-possible-to-get-russian-characters-from-pdf
		# Idea for the code from: https://www.codegrepper.com/code-examples/python/UnicodeEncodeError%3A+%27charmap%27+codec+can%27t+encode+character+%27%5Cu2764%27+in+position+24925%3A
        make_new_text_file.write(text)
        make_new_text_file.close()
    outfp.close()

#Get the pdf file name in the folder and list it
for name in pdf_file_name:
	if pdf_checker(name):
		try:
			convert_pdf_to_txt(name, name + '.txt')		# pdf_Use checker and TRUE (end is.For pdf) proceed to conversion)
			# 78 luo virheen ja se pitää korjata, jollakin "pass" None parmaterilla
		except:
			pass
