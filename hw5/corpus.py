from app import app
from flask import flash, render_template, request, redirect, g
from app import forms
import sqlite3 as sql
from pymystem3 import Mystem

DATABASE = 'corpus.db'
mystem = Mystem()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    return db


@app.route('/', methods=['GET', 'POST'])
def index():
    search = forms.SearchForm(request.form)
    if request.method == 'POST':
        return results(search)
    return render_template('main.html', form=search)


@app.route('/results')
def results(search):
    search_string = search.data['search']
    search_string = mystem.lemmatize(search_string)[0]
    qry_url = 'SELECT url FROM corpus WHERE lemma_texts LIKE "%' + search_string + '%"'
    qry_text = 'SELECT plain_texts FROM corpus WHERE lemma_texts LIKE "%' + search_string + '%"'
    c = get_db().cursor()
    c.execute(qry_url)
    res_url = c.fetchall()
    res_url = [str(a[0]) for a in res_url]
    c.execute(qry_text)
    res_text = c.fetchall()
    res_text = [' '.join(str(a[0]).split(' ')[:100]) for a in res_text]

    return render_template('results.html', res=zip(res_url, res_text))
