from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PWORD_REGEX = re.compile(r'(?=^.{8,}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&amp;*()_+}{&quot;:;\'?/&gt;.&lt;,])(?!.*\s).*$')

app = Flask(__name__)

app.secret_key = "secret"

@app.route('/', methods=['GET'])
def index():
	return render_template('registration.html')

@app.route('/process', methods=['POST'])
def process():
	session['class'] = 'red'
	if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm']) < 1:
		flash("Please fill out all fields")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address")
	elif not NAME_REGEX.match(request.form['first_name']) or not NAME_REGEX.match(request.form['last_name']):
		flash("Invalid Name entry")
	elif not PWORD_REGEX.match(request.form['password']):
		flash("Password must be at least 8 characters and include one uppercase letter, one lowercase letter, and one special character")
	elif not request.form['password'] == request.form['confirm']:
		flash("Passwords do not match")
	else:
		session['class'] = 'green'
		flash("Registration success!")
	return redirect ('/')

app.run(debug=True)