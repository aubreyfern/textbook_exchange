from flask import Flask, request, render_template, redirect, url_for
import pymysql
from wtforms import Form, StringField, SelectField
import config

app = Flask(__name__)

db = config.Database
db.__init__(db)



@app.route('/',methods=['GET','POST'])
def index():
    search = searchForm(request.form)
    if request.method == 'POST':
        return search

    return render_template('login.html', form=search)

@app.route('/donate',methods=['GET','POST'])
def donate():
    search = searchForm(request.form)
    if request.method == 'POST':
        return search

    return render_template('donate.html', form=search)

