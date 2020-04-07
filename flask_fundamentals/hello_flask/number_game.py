from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'thisissecret'
@app.route('/')         
def index():
    
    colors = 'red'
    texts = ''
    play_again = 'none'
    if 'visibility' in session:
        visible = session['visibility']
    else:
        visible ='none'
    if 'colors' in session:
        colors = session['colors']    
    if 'text' in session:
        texts = session['text']
    if 'button' in session:
        play_again = session['button']
    
    return render_template("number_game.html", visibility = visible, color = colors, text = texts, btnvisibility=play_again)

@app.route('/result', methods=['POST'])
def result():
    if 'random' in session:
        pass
    else:
        session['random'] = random.randrange(0,101)

    session['guess'] = float(request.form['number'])
    session['visibility'] = 'block'
    if session['guess'] < session['random']:
        session['colors'] = 'red'
        session['text'] = "Too low!"
        session['visibility'] = 'block'
    if session['guess'] > session['random']:
        session['colors'] = 'red'
        session['text'] = "Too High!"
        session['visibility'] = 'block'
    if session['guess'] == session['random']:
        session['colors'] = 'green'
        session['text'] = str(session['random']) + ' was the number!'
        session['button'] = 'inline'
        session['visibility'] = 'block'

    print(session['random'])
    return redirect('/')
    

@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect("/")
if __name__=="__main__":   
    app.run(debug=True)    