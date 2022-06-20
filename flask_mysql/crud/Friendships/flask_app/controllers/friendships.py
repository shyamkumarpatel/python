from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.Friendship import Friendship

@app.route("/newFriendship", methods=["POST"])
def add_new_friendship():
    last_id_inserted = Friendship.addNewFriendship(request.form)
    return redirect("/friendships")