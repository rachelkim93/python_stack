from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z- ]+$')

@app.route('/')
def Form():
    if 'fname' not in session:
        session['fname'] = ""
    if 'lname' not in session:
        session['lname'] = ""
    if 'email' not in session:
        session['email'] = ""
    return render_template("login_regist.html")

@app.route('/register', methods=['POST'])
def Register():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    confirm_pw = request.form['confirm_pw']
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    session['status'] = "valid"
    if len(fname) < 2:
        session['status'] = "invalid"
        flash(u'First name must be atleast 2 characters and only consist of letters.', 'fname')
    elif not NAME_REGEX.match(fname):
        session['status'] = "invalid"
        flash(u'Name can only contain letters, spaces, or hyphens.', 'fname_chars')
    else:
        session['fname'] = fname 
    if len(lname) < 2:
        session['status'] = "invalid"
        flash(u'Last name must be atleast 2 characters and only consist of letters.', 'lname')
    elif not NAME_REGEX.match(lname):
        session['status'] = "invalid"
        flash(u'Name can only contain letters, spaces, or hyphens.', 'lname_chars')
    else:
        session['lname'] = lname
    if not EMAIL_REGEX.match(email):
        session['status'] = "invalid"
        flash(u'Invalid email address.', 'email')
    else:
        session['email'] = email
    if len(password) < 8:
        session['status'] = "invalid"
        flash(u'Password must be atleast 8 characters.', 'pass_length')
    elif re.search('[0-9]', password) is None:
        session['status'] = "invalid"
        flash(u'Password must contain atleast one digit (0-9).', 'pass_digit')
    elif re.search('[A-Z]', password) is None:
        session['status'] = "invalid"
        flash(u'Password must contain atleast one capital letter', 'pass_cap')    
    if confirm_pw != password:
        session['status'] = "invalid"
        flash(u'Does not match password.', 'confirm_pw')
    elif session['status'] == "valid":
        mysql = connectToMySQL("loginregistration")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        data = {
                'first_name': fname,
                'last_name': lname,
                'email': email,
                'password': pw_hash
                }
        new_user_id = mysql.query_db(query, data)
        return redirect('/success')
    return redirect('/')

@app.route('/login', methods=['POST'])
def Login():
    email = request.form['email']
    password = request.form['password']
    mysql = connectToMySQL("loginregistration")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
            'email': email
        }
    return_user = mysql.query_db(query, data)
    print(return_user)
    if len(return_user) < 1:
        session['status'] = "invalid"
        flash(u'Check email address and password.', 'login')
        return redirect('/')
    if bcrypt.check_password_hash(return_user[0]['password'], password):
        session['fname'] = return_user[0]['first_name']
        session['status'] = "logged_in"
        return redirect('/success')

@app.route('/success')
def Success():
    return render_template("success.html")

@app.route('/logout')
def Logout():
    session.clear()
    return redirect('/')

app.run(debug=True)