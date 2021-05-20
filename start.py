import pickle
import numpy as np
from flask import Flask, request, jsonify, redirect, url_for, abort, render_template
from sklearn import datasets
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from catboost import CatBoostRegressor

import predict



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
    try:
        if request.method == 'POST':
            password = request.form['password']
            if password =='':
                abort(400)
            model = pickle.load(open('model', 'rb'))
            prediction = predict.predict(password, model)
            img = 'static/'
            if prediction > 50:
                img += 'lol.png'
            else:
                img += 'not-bad.jpg'
            return render_template('submit.html', \
                form=form, prediction=prediction, img=img)

            #return form.data['name']
        return render_template('submit.html', form=form)
    except Exception:
        abort(400)