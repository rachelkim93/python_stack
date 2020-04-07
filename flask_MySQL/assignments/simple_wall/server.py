from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import datetime
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
    return render_template("simple_wall.html")

@app.route('/register', methods=['POST'])
def Register():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    confirm_pw = request.form['confirm_pw']
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    session['status'] = "valid"
    mysql = connectToMySQL("simplewall")
    query = "SELECT email FROM users WHERE email = %(email)s;"
    data = {
            'email': email
        }
    email_check = mysql.query_db(query, data)
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
    if len(email_check) > 0:
        session['status'] = "invalid"
        flash(u'Email address already registered', 'email_reg')
    elif not EMAIL_REGEX.match(email):
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
        mysql = connectToMySQL("simplewall")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        data = {
                'first_name': fname,
                'last_name': lname,
                'email': email,
                'password': pw_hash
                }
        new_user_id = mysql.query_db(query, data)
        mysql = connectToMySQL("simplewall")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {
                'email': email
            }
        return_user = mysql.query_db(query, data)
        session['id'] = return_user[0]['id']
        return redirect('/wall')
    return redirect('/')

@app.route('/login', methods=['POST'])
def Login():
    email = request.form['email']
    password = request.form['password']
    mysql = connectToMySQL("simplewall")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
            'email': email
        }
    return_user = mysql.query_db(query, data)
    if len(return_user) < 1:
        session['status'] = "invalid"
        flash(u'Check email address and password.', 'login')
        return redirect('/')
    if bcrypt.check_password_hash(return_user[0]['password'], password):
        session['fname'] = return_user[0]['first_name']
        session['id'] = return_user[0]['id']
        session['status'] = "logged_in"
        return redirect('/wall')

@app.route('/wall')
def UsersQuery():
    mysql = connectToMySQL("simplewall")
    query = "SELECT id, first_name, last_name, email FROM users WHERE id != %(id)s;"
    data = {
            'id': session['id']
        }
    other_users = mysql.query_db(query, data)
    mysql = connectToMySQL("simplewall")
    query = "select messages.id, sender_id, message, users.first_name, messages.created_at FROM messages JOIN users on users.id = messages.sender_id where recipient_id = %(id)s ORDER BY messages.created_at DESC"
    data = {
            'id': session['id']
        }
    return_messages = mysql.query_db(query, data)
    for x in return_messages:
        print(x)
        print("hello")
        print(x['created_at'])
        created = x['created_at']
        msg_date = created.strftime("%j")
        print(msg_date)
        x['created_at'] = msg_date
    print(return_messages)
    mysql = connectToMySQL("simplewall")
    query = "SELECT count(sender_id) FROM messages WHERE sender_id = %(id)s;"
    data = {
            'id': session['id']
        }
    return_sent = mysql.query_db(query, data)
    mysql = connectToMySQL("simplewall")
    query = "SELECT count(recipient_id) FROM messages WHERE recipient_id = %(id)s;"
    data = {
            'id': session['id']
        }
    return_received = mysql.query_db(query, data)
 
    now = datetime.datetime.now()
    day = now.strftime("%j")
    print(day)
    return render_template("wall.html", users = other_users, messages = return_messages, outbound = return_sent, received = return_received, d = day)

@app.route('/send', methods=['POST'])
def Post():
    print(request.form)
    message = request.form['message']
    id = request.form['recipient_id']
    mysql=connectToMySQL("simplewall")
    query = "INSERT INTO messages (sender_id, recipient_id, message, created_at, updated_at) VALUES (%(sender)s, %(recipient)s, %(msg)s, NOW(), NOW());"
    data = {
            'sender': session['id'],
            'recipient': id,
            'msg': message
            }
    print_messages = mysql.query_db(query, data)
    print(print_messages)
    return redirect('/wall')

@app.route('/delete', methods=['POST'])
def Delete():
    mysql = connectToMySQL("simplewall")
    id = request.form['delete']
    query = "DELETE FROM messages WHERE id = %(id)s"
    data = {
            'id': id
        }
    delete_msg = mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/logout')
def Logout():
    session.clear()
    return redirect('/')

app.run(debug=True)