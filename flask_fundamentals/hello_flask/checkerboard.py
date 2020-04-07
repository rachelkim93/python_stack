from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def checkerboard():
    return render_template("checkerboard.html", x=8, y=8)

@app.route('/<x>/<y>')
def multiple(x, y):
    return render_template("checkerboard.html", x=int(x), y=int(y))


if __name__=="__main__":
    app.run(debug = True)