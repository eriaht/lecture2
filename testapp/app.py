import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    headline = 'Welcome to the test site haha'
    return render_template('index.html', headline=headline)

@app.route('/bday')
def bday():
    now = datetime.datetime.now()
    bday = now.month == 5 and now.day == 12
    return render_template('bday.html', bday=bday)

@app.route('/gang')
def ganggang():
    return 'gang gang'

@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return f'<h1>Hello, {name}.</h1>'
