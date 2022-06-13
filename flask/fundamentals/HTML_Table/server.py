from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",rows=8, cols=8, boxColor="black",boxColor2="red")

    
if __name__=="__main__":
    app.run(debug=True) 