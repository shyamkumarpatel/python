from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",times=3)


@app.route('/<int:x>')
def play(x):
    return render_template("index.html",times= x, boxColor="aqua")

@app.route('/<int:x>/<color>')
def playColor(x,color):
    print("----------Server Print Statment, Color:", color)
    return render_template("index.html",times= x,boxColor = color)

if __name__=="__main__":
    app.run(debug=True) 
