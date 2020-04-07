
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def counter():
   try:
      session['counter'] += 1
   except KeyError:
      session['counter'] = 1
   return render_template('counter.html', counter = session['counter'])

@app.route('/add', methods=['POST'])
def add():
    if request.form['button'] == 'counter':
        session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if request.form['button'] == 'reset':
        session['counter'] = 0
    return redirect('/')

app.run(debug = True)