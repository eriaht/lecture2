from flask import Flask, render_template, request, session
from flask_session.__init__ import Session

app = Flask(__name__)
app.degub = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET','POST'])
def index():
    if session.get('notes') is None:
        # session is a dictionary
        session['notes'] = []
    if request.method == 'POST':
        note = request.form.get('note')
        session['notes'].append(note)

    return render_template('index.html', notes=session['notes'])
