from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/play')
def playground():
    return render_template("playground.html", number=3)

@app.route('/play/<number>')
def multiple(number):
    return render_template("playground.html", number=int(number))

if __name__=="__main__":
    app.run(debug = True)
