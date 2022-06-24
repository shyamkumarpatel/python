from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.Recipe import Recipe
from flask_app.models.User import User
import datetime

@app.route("/recipes/new")
def load_create_page():
    if User.validate_session() == True:
        return render_template("createRecipe.html")
    else:
        return redirect("/login")

@app.route("/create", methods=["POST"])
def create_recipe():
    if User.validate_session() == False:
        return redirect("/login")
    else:
        print("Request Form --> ", request.form)
        if Recipe.validate_create_recipe(request.form):
            data = {
                'name': request.form['name'], 
                'description': request.form['description'], 
                'instructions': request.form['instructions'], 
                'date_made': request.form['date_made'],  
                'under30mins': request.form['under30mins'], 
                'users_id': session['id']
            }
            Recipe.addNewRecipe(data)
            return redirect("/dashboard")
        else:
            return redirect("/recipes/new")

@app.route("/recipes/<int:recipe_id>")
def view_recipe(recipe_id):
    if User.validate_session() == False:
        return redirect("/login")
    else:
        data={'id':recipe_id}
        recipe_info = Recipe.getRecipe(data)
        recipe_info2 = {
            'id': recipe_info.id, 
            'name': recipe_info.name, 
            'description':recipe_info.description, 
            'instructions': recipe_info.instructions, 
            'date_made': recipe_info.date_made.strftime("%B %d, %Y"),  
            'under30mins': 'Yes' if recipe_info.under30mins == 1 else 'No', 
            'users_id': recipe_info.users_id
        }
        return render_template("viewRecipe.html", recipe = recipe_info2)

@app.route("/recipes/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    if User.validate_session() == False:
        return redirect("/login")
    else:
        data={'id':recipe_id}
        recipe_info = Recipe.getRecipe(data)
        recipe_info2 = {
            'id': recipe_info.id, 
            'name': recipe_info.name, 
            'description':recipe_info.description, 
            'instructions': recipe_info.instructions, 
            'date_made': recipe_info.date_made.strftime("%B %d, %Y"),  
            'under30mins': 'Yes' if recipe_info.under30mins == 1 else 'No', 
            'users_id': recipe_info.users_id
        }
        return render_template("updateRecipe.html", recipe = recipe_info)

@app.route("/update", methods=["POST"])
def update_recipe():
    if User.validate_session() == False:
        return redirect("/login")
    else:
        print("Request Form --> ", request.form)
        # data = {
        #     'name': request.form['name'], 
        #     'description': request.form['description'], 
        #     'instructions': request.form['instructions'], 
        #     'date_made': request.form['date_made'],  
        #     'under30mins': request.form['under30mins'], 
        #     'users_id': session['id']
        # }
        Recipe.editRecipe(request.form)
        return redirect("/dashboard")

@app.route("/recipes/delete/<int:recipe_id>")
def delete_recipe(recipe_id):
    if User.validate_session() == False:
        return redirect("/login")
    else:
        data={'id':recipe_id}
        recipe_info = Recipe.deleteRecipe(data)
        print(recipe_info)
        return redirect("/dashboard")