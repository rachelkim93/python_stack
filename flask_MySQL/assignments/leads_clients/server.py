from flask import Flask, render_template, request, redirect, session

from leads_clients import connectToMySQL

app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def Dash():
    mysql = connectToMySQL("lead_gen_business")
    leads = mysql.query_db("SELECT * FROM leads")
    session['leads'] = leads
    print(leads)
    return render_template("leads_clients.html", lead = leads)

app.run(debug=True)