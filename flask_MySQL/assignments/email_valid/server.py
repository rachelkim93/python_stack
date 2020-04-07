from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL 
app = Flask(__name__)
app.secret_key="ThisIsSecret"

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')

@app.route('/')
def Home():
    if 'valid' not in session:
        session['valid'] = "none"
    return render_template("email_valid.html")

@app.route('/valid', methods=['POST'])
def Valid():
    mysql = connectToMySQL("emaildb")
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash('*Must enter a valid email')
        session['valid'] = "invalid"
        return redirect('/')
    elif EMAIL_REGEX.match(email):
        session['valid'] = "valid"
        session['email'] = email
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW());"
        data = {
                'email': email, 
            }
        new_email_id = mysql.query_db(query, data) 
        return redirect('/success')

@app.route('/success')
def Success():
    mysql = connectToMySQL("emaildb")
    emails = mysql.query_db("SELECT * FROM emails")
    print(emails)
    return render_template("success.html", emailsarr = emails)

@app.route('/delete', methods=['POST'])
def Delete():
    mysql = connectToMySQL("emaildb")
    email = session['email']
    session['valid'] = "delete"
    query = "DELETE FROM emails WHERE email = (%(email)s)"
    data = {
            'email': session['email']
        }
    delete_email = mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)