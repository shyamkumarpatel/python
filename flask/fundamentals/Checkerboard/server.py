from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",rows=8, cols=8, boxColor="black",boxColor2="red")


@app.route('/<int:x>')
def displayNumsRows(x):
    return render_template("index.html",rows=x, cols=8, boxColor="black",boxColor2="red")

@app.route('/<int:x>/<int:y>')
def displayNumsRowsCols(x,y):
    return render_template("index.html",rows=x, cols=y, boxColor="black",boxColor2="red")

@app.route('/<int:x>/<int:y>/<color>')
def displayNumsRowsColsColor(x,y,color):
    return render_template("index.html",rows=x, cols=y, boxColor=color,boxColor2="red")

@app.route('/<int:x>/<int:y>/<color>/<color2>')
def displayNumsRowsColsColors(x,y,color,color2):
    return render_template("index.html",rows=x, cols=y, boxColor=color,boxColor2=color2)

if __name__=="__main__":
    app.run(debug=True) 