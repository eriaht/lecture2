import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET','POST'])
def hello():
    # If user requests /hello send them back to index.html.
    if request.method == 'GET':
        return render_template('index.html')

    now = datetime.datetime.now()
    # Slicing the year off of the form data (0000-).
    birthdate = request.form.get("birthdate")[5:]
    today = f"{now.month}-{now.day}"
    is_birthday = today == birthdate
    print(is_birthday)
    print(birthdate)

    return render_template('hello.html', is_birthday=is_birthday)