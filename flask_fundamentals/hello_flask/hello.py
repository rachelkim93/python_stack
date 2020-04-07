from flask import Flask, render_template, request
app = Flask(__name__)

print(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<Flask>')
def say(Flask):
    return "Hi, " + Flask

@app.route('/repeat/<rep>/<hello>')
def repeat(hello, rep):
    return ((hello+"\n")*int(rep))

if __name__=="__main__":
    app.run(debug = True)