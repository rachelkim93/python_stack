
from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def gameView():
	try:
		if session['gold'] < 0: #if the user's gold is negative...
			session['goldColor'] = 'red' #make the gold displayed red
		else: #if it's positive...
			session['goldColor'] = '' #go back in the black!
	except KeyError: #if these values are not yet defined...
		session['gold'] = 0 #start the user at 0 gold
		session['goldColor'] = '' #the color should be black
		session['activities'] = [] #and activities should be empty
	return render_template('ninja_gold.html')

@app.route('/makeGold', methods=['POST'])
def makeGold():
	session['time'] = datetime.datetime.now() #when the button is pressed, log the current time
	session['place'] = request.form['place'] #record the place clicked
	places = { #initialize and declare an object to hold places
		'farm' : random.randint(10,20), #the farm will generate a random amount of gold between 10 and 20
		'cave' : random.randint(5,10), #the cave will generate a random amount of gold between 5 and 10
		'house' : random.randint(2,5), #the house will generate a random amount of gold between 2 and 5
		'casino' : random.randint(-50,50), #the casino will generate a random amount of gold between -50 and 50
	}
	session['result'] = places[session['place']] #set result to the gold generated
	if session['result'] >= 0: #if the amount of gold generated is greater than or equal to 0...
		session['activity'] = { #create a new object...
			'class' : 'green', #set the class key to green
			'activity' : 'Earned {} golds from the {}!'.format(session['result'], session['place']), #define the value of the displayed string
			'time' : session['time'], #set the time equal to the time stamp
		}
	else: #if the amount of gold generated is less than 0...
		session['activity'] = {
			'class' : 'red',
			'activity' : 'You entered a {} and lost {} golds... Ouch...'.format(session['place'], session['result']),
			'time' : session['time'],
		}
	session['activities'].insert(0, session['activity']) #prepend the object created to the activities list
	session['gold'] += session['result'] #the gold generated should be added to the user's gold
	return redirect('/') #return to the / route

@app.route('/reset')
def restart(): #reset the game
	session['gold'] = 0
	session['activities'] = []
	return redirect('/')

app.run(debug=True)