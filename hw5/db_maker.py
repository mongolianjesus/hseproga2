import glob
import pandas as pd
import sqlite3 as db
filelist_plain = glob.glob('corpus/plain/*/*/*.txt')
filelist_lemmas = glob.glob('corpus/mystem-plain/*/*/*.txt')
plain_texts = []
lemma_texts = []

for f in filelist_plain:
    with open(f, 'r', encoding='utf-8') as fl:
        text = fl.read()
        plain_texts.append(text)


for f in filelist_lemmas:
    with open(f, 'r', encoding='utf-8') as fl:
        text = fl.read()
        lemma_texts.append(text)


df = pd.DataFrame()
df['plain_texts'] = pd.Series(plain_texts)
df['lemma_texts'] = pd.Series(lemma_texts)
df['url'] = df['plain_texts'].str.extract(r'@url (http.+\.html)')
df['title'] = df['plain_texts'].str.extract(r'@ti (.+)\n@')
df['plain_texts'] = df['plain_texts'].str.replace(r'@.+?\n', '')


conn = db.connect('corpus.db')
df.to_sql('corpus', con=conn)
