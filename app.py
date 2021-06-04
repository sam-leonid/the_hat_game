import json
import os
import random

import fasttext

from player.player import LocalFasttextPlayer

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


#from flask import Flask, request, jsonify, redirect, url_for, abort, render_template



from player.player import LocalFasttextPlayer



player = LocalFasttextPlayer(model=fasttext.load_model("models/skipgram2.model"))

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

class MyForm(FlaskForm):
    name = StringField('your password', validators=[DataRequired()])

@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    return render_template('submit.html', form=form)

@app.route("/explain")
def explain():
    word = request.args.get("word")
    n_words = int(request.args.get("n_words"))
    return json.dumps(player.explain(word=word, n_words=n_words))


@app.route("/guess")
def guess():
    words = request.args.getlist("words")
    n_words = int(request.args.get("n_words"))
    return json.dumps(player.guess(words=words, n_words=n_words))
