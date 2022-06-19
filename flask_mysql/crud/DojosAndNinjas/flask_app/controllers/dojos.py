from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.model.Dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def getdojos():
    Dojos = Dojo.get_all()
    return render_template("index.html", all_Dojos = Dojos)

@app.route("/dojos/<int:id>")
def getNinjaInfo(id):
    data={'id':id}
    #dojo_name = Dojo.getDojo(data)
    ninja_info = Dojo.getDojoNinjas(data)
    return render_template("dojo_show.html", Dojo_Ninjas = ninja_info)

@app.route("/newdojo", methods=["POST"])
def add_new_dojo():
    last_id_inserted = Dojo.addNewDojo(request.form)
    return redirect("/dojos")