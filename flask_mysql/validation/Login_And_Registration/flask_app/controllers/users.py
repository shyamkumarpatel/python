from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.User import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login")
def users():
    if User.validate_session() == True:
        return redirect("/dashboard")
    else:
        return render_template("index.html")


@app.route("/login", methods=["POST"])
def login_user():
    if User.validate_login(request.form) == False:
        return redirect("/login")
    else:
        # create the hash
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            "email" : request.form['email'],
            "password" : pw_hash
        }
        result = User.getUser(data)
        
    if result == None:
        flash("Wrong credentials", "error_login")
        return redirect("/login")
    else:
        session['first_name'] = result.first_name
        session['last_name'] = result.last_name
        session['email'] = result.email
        session['id'] = result.id
        return redirect("/dashboard")

@app.route("/dashboard")
def view_dashboard():
    if User.validate_session() == True:
        return redirect("/dashboard")
    else:
        return redirect("/login")

@app.route("/addUser", methods=["POST"])
def add_new_user():
    if User.validate_registration(request.form):
        # create the hash
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        # put the pw_hash into the data dictionary
        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "password" : pw_hash
        }
        user_id = User.addNewUser(data)
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        session['id'] = user_id
        return redirect("/dashboard")
    else:
        return redirect("/login")

@app.route("/logout")
def user_logout():
    session.clear()
    return redirect("/login")
