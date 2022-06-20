from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.User import User
from flask_app.models.Friendship import Friendship

@app.route("/")
def index():
    return redirect("/friendships")

@app.route("/friendships")
def getUsers():
    all_friendships = Friendship.get_all()
    all_users = User.get_all()
    print(User.getUserFriendships({'id':1}))
    return render_template("index.html", all_users = all_users, all_friendships = all_friendships)

@app.route("/addUser", methods=["POST"])
def add_new_dojo():
    last_id_inserted = User.addNewUser(request.form)
    print(last_id_inserted)
    return redirect("/friendships")

# @app.route("/dojos/<int:id>")
# def getNinjaInfo(id):
#     data={'id':id}
#     #dojo_name = Dojo.getDojo(data)
#     ninja_info = Dojo.getDojoNinjas(data)
#     return render_template("dojo_show.html", Dojo_Ninjas = ninja_info)

# @app.route("/newdojo", methods=["POST"])
# def add_new_dojo():
#     last_id_inserted = Dojo.addNewDojo(request.form)
#     return redirect("/dojos")