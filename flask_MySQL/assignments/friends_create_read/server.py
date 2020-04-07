from flask import Flask, request, redirect, render_template, session, flash

from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    mysql = connectToMySQL("friendsdb")
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('friends_create_read.html', friends = all_friends)

@app.route('/friends', methods=['POST'])
def create():
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW())"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation']
           }

    new_friend_id = mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)