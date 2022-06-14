from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "num_of_visits" in session:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)