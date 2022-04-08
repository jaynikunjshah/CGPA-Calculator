import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def name():
    if request.method == 'GET':
        return render_template('cgpacalc.html')
    else:
        x = int(request.form.get('subj'))
        return render_template("calc.html",subj = x)