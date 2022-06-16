from flask import Flask, render_template, redirect, request
# import the class from friend.py
from Users import User

app = Flask(__name__)
@app.route("/")
def index():
	return redirect("/users")

@app.route("/users")
def users():
	Users = User.get_all()
	#print("----------------Getting Users----------------------\n",Users,"\n------------------------------------------------------")
	return render_template("index.html", all_users = Users)

@app.route("/new")
def add_user():
	return render_template("addUser.html")

@app.route("/new", methods=["POST"])
def add_new_user():
	print(User.addNewUser(request.form))
	return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)