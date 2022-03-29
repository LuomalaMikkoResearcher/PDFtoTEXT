# Author: Mikko Luomala 
# Version:

# Python load the libaries for creating dataframe, exploring datasets and spacy NLP machine learning library
import pandas as pd
import glob, os, re,  codecs
import spacy
import deplacy
import en_core_web_sm
nlp = spacy.load("en_core_web_sm")
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from pathlib import Path

from tkinter import Tk
import tkinter as tk

from tkinter.filedialog import askdirectory
print("Select Folder drive for where the input folder of the research datasets are located")
datasets = askdirectory(title='Select Folder for where the datasets files are') # shows dialog box and return the path

### Global variables ###
i = 0 # Luodaan juoksevanumero
### Global variables end ###


header = ['Names of PDFS','Clauses of search'] # 'Year' removed, because datasets filename has year 2021 and not absolute year numbers of publications.
df=pd.DataFrame(columns=['Names of PDFS','Clauses of search']) # 'Year' removed, because datasets filename has year 2021 and not absolute year numbers of publications.
df.set_index('Names of PDFS')



# I set filename list to df['|Names of PDFS|']

pdcsv = Path("I:\\Essee\\prevention_23032022.csv") # On Windows system you have to put \\ so that path diring works
pdcsv.parent.mkdir(parents=True, exist_ok=True)

# Function to for parsing the dataset
# For loop for computing the datasets and selecting clauses from datasets with keyword
def parse():
    with codecs.open(file,'r', encoding='utf-8',errors='ignore') as f:
        global i
        text = f.read()
        phrase_matcher = PhraseMatcher(nlp.vocab)
        phrases = ['prevention'] # The keyword for the searches of clauses
        patterns = [nlp(text) for text in phrases]
        phrase_matcher.add('AI', None, *patterns)
        nlp.max_length = len(text) + 100
        doc = nlp(text)
        for sent in doc.sents:
            for match_id, start, end in phrase_matcher(nlp(sent.text)):
                if nlp.vocab.strings[match_id] in ["AI"]:
                    print(sent.text)
                    #print(file)
                    df.loc[i,'Clauses of search'] = sent.text  # reading the data and adding running number to dataframe of Panda
                    df.loc[i,'Names of PDFS']= file
                    #m = re.search(r"[0-9][0-9][0-9][0-9]", file) # reading the file name and selecting four digits (year)
                    #df.loc[i,'Year'] = m.group() # selecting the year name of the file
                    #df.insert(loc=3, column="Stars", value=file) # implementing read text file name to column of Names of PDFS
                    # column name of year is removed from dataframe, because it does not work.
                    i += 1
                    #print(i)
# Selecting the datasets
os.chdir(datasets)

files = glob.glob('*.txt') # Selecting the datasets *.txt files
for file in files: # For loop for computing the datasets and selecting clauses from datasets with keyword
    parse()
    print(file) # Printing processed filenames

df.to_csv(pdcsv,sep=';',encoding='utf-8')  # We are extracting the data to csv file on the left side is running number, middle dataset name and clauses of datasets
# fixed because error, but not tested. Will utf-8 work better.
# ISO-8859-1 or utf-8 or cp1252 is needed on Windows enviroment so that the output data is stored without errors on the text
# df.to_csv(pdcsv,sep=';',encoding='ISO-8859-1')  # We are extracting the data to csv file on the left side is running number, middle dataset name and clauses of datasets
# UnicodeEncodeError: 'latin-1' codec can't encode character '\u2013' in position 215: ordinal not in range(256)
# cp1252 encoding makes text readable when it is stored in csv file.
print("End of the Test")
print (df)
print("End of the Test")

# Error code 27.3.2022 klo 14:56
#9_information_security_autunm_2021.txt
#Traceback (most recent call last):
#  File "I:\Essee\prevention.py", line 70, in <module>
#    df.to_csv(pdcsv,sep=';',encoding='cp1252')  # We are extracting the data to csv file on the left side is running number, middle dataset name and clauses of datasets
#  File "C:\Users\media\anaconda3\envs\tf-gpu\lib\site-packages\pandas\core\generic.py", line 3563, in to_csv
#    return DataFrameRenderer(formatter).to_csv(
#  File "C:\Users\media\anaconda3\envs\tf-gpu\lib\site-packages\pandas\io\formats\format.py", line 1180, in to_csv
#    csv_formatter.save()
#  File "C:\Users\media\anaconda3\envs\tf-gpu\lib\site-packages\pandas\io\formats\csvs.py", line 261, in save
#    self._save()
#  File "C:\Users\media\anaconda3\envs\tf-gpu\lib\site-packages\pandas\io\formats\csvs.py", line 266, in _save
#    self._save_body()
#  File "C:\Users\media\anaconda3\envs\tf-gpu\lib\site-packages\pandas\io\formats\csvs.py", line 304, in _save_body
#    self._save_chunk(start_i, end_i)
#  File "C:\Users\media\anaconda3\envs\tf-gpu\lib\site-packages\pandas\io\formats\csvs.py", line 315, in _save_chunk
#    libwriters.write_csv_rows(
#  File "pandas\_libs\writers.pyx", line 55, in pandas._libs.writers.write_csv_rows
#  File "C:\Users\media\anaconda3\envs\tf-gpu\lib\encodings\cp1252.py", line 19, in encode
#    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
#UnicodeEncodeError: 'charmap' codec can't encode character '\u02ab' in position 93: character maps to <undefined>
#(tf-gpu) I:\Essee>
