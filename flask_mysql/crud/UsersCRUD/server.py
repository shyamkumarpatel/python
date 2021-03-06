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
	last_id_inserted = User.addNewUser(request.form)
	return redirect(f"/users/{last_id_inserted}")

@app.route("/users/<int:id>")
def getUserInfo(id):
	data={'id':id}
	user_info = User.getUser(data)
	return render_template("viewUser.html", user = user_info[0])


@app.route("/users/<int:id>/edit")
def editUser(id):
	data={'id':id}
	user_info = User.getUser(data)
	return render_template("editUser.html",  user = user_info[0])

@app.route("/users/<int:id>/edit", methods=["POST"])
def editUserInfo(id):
	user_info = User.updateUser(request.form)
	return redirect(f"/users/{id}")

@app.route("/users/<int:id>/delete")
def deleteUser(id):
	data={'id':id}
	User.deleteUser(data)
	return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)