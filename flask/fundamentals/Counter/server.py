from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html",numCount = 1)

    
if __name__=="__main__":
    app.run(debug=True) 