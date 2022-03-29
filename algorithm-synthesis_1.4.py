# Idea for the code from: https://github.com/Raks-coder/NLP-Tutorial-12---Text-Summarization-using-NLP/blob/master/Text%20Summarization%20using%20NLP.ipynb

import spacy, os # Myself added
import pandas as pd  # Myself added
from pathlib import Path  # Myself added
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')


with open('synthesis_dataset.txt',encoding='utf-8') as f:  # Myself added
    text = f.read()  # Myself added
    nlp.max_length = len(text) + 100  # Myself added. Otherwise algorithm gives error that 1 Gb memory limit is exceeded.
    doc = nlp(text)  # Myself added

tokens = [token.text for token in doc]
print("tokens",tokens) # I modified the code by adding printing
df1 = pd.DataFrame({"Tokens": [tokens]}) # Myself added

punctuation = punctuation + '\n'

print("punctuation",punctuation) # I modified the code by adding printing
df2 = pd.DataFrame({"Punctuation": [punctuation]}) # Myself added

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

print(word_frequencies) # I modified the code by adding printing

max_frequency = max(word_frequencies.values())

print("Max frequency",max_frequency) # I modified the code by adding printing
df3 = pd.DataFrame({"Max frequency": [max_frequency]}) # Myself added

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

print(word_frequencies)  # Myself added
df4 = pd.DataFrame({"Word frequencie": [word_frequencies]}) # Myself added

sentence_tokens = [sent for sent in doc.sents]
print(sentence_tokens)  # Myself added
df5 = pd.DataFrame({"sentence tokens": [sentence_tokens]})# Myself added


sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]

print("Scores of the sentences",sentence_scores) # I modified the code by adding printing

df6 = pd.DataFrame({"Scores of the sentences": [sentence_scores]}) # Myself added


select_length = int(len(sentence_tokens)*0.3)
print("Select length",select_length)

df7 = pd.DataFrame({"Select length": [select_length]}) # Myself added

summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

print("Summary",summary) # I modified the code by adding printing



final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
print(text)
print(summary)

df8 = pd.DataFrame({"Summary Synthesis": [summary]}) # Myself added

len(text)
len(summary)

pdcsv1 = Path("L:\\df1.csv")  # Myself added
df1.to_csv(pdcsv1,sep=';',encoding='utf-8')  # Myself added
pdcsv2 = Path("L:\\df2.csv")  # Myself added
df2.to_csv(pdcsv2,sep=';',encoding='utf-8')  # Myself added
pdcsv3 = Path("L:\\df3.csv")  # Myself added
df3.to_csv(pdcsv3,sep=';',encoding='utf-8')  # Myself added
pdcsv4 = Path("L:\\df4.csv")  # Myself added
df4.to_csv(pdcsv4,sep=';',encoding='utf-8')  # Myself added
pdcsv5 = Path("L:\\df5.csv")  # Myself added
df5.to_csv(pdcsv5,sep=';',encoding='utf-8')  # Myself added
pdcsv6 = Path("L:\\df6.csv")  # Myself added
df6.to_csv(pdcsv6,sep=';',encoding='utf-8')  # Myself added
pdcsv7 = Path("L:\\df7.csv")  # Myself added
df7.to_csv(pdcsv7,sep=';',encoding='utf-8')  # Myself added
pdcsv8 = Path("L:\\df8.csv")  # Myself added
df8.to_csv(pdcsv8,sep=';',encoding='utf-8')  # Myself added
