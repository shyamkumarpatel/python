from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.model.Dojo import Dojo
from flask_app.model.Ninja import Ninja

@app.route("/ninjas")
def add_ninja():
    Dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_Dojos = Dojos)

@app.route("/ninjas", methods=["POST"])
def add_new_ninja():
    last_id_inserted = Ninja.addNewNinja(request.form)
    print(last_id_inserted)
    return redirect("/dojos")