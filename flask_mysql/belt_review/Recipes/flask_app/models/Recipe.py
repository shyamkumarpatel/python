from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
class Recipe:
    def __init__( self , data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30mins = data['under30mins']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes; "
        results = connectToMySQL('recipes_schema').query_db(query)
        print("results", results)
        Recipes = []
        
        for recipe in results:
            Recipes.append( cls(recipe) )
        return Recipes

    @classmethod
    def addNewRecipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under30mins, date_made, users_id)"
        query += "VALUES ( %(name)s,  %(description)s ,  %(instructions)s ,  %(under30mins)s ,  %(date_made)s, %(users_id)s);"
        lastInsertedRowID = connectToMySQL('recipes_schema').query_db(query, data)
        print(lastInsertedRowID)
        return lastInsertedRowID

    @classmethod
    def getRecipe(cls, data):
        query = "select * FROM recipes "
        query += "WHERE id = %(id)s ;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def editRecipe(cls, data):
        query = "UPDATE recipes "
        query += " SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, "
        query += " under30mins = %(under30mins)s, date_made = %(date_made)s "
        query += " WHERE id = %(id)s ;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results

    @classmethod
    def deleteRecipe(cls, data):
        query = "DELETE FROM recipes "
        query += "WHERE id = %(id)s ;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_create_recipe(data):
        print("---Data-----::: ",data)
        isValid = True
        if  len(data['name']) < 3:
            flash("You must provide name with at lease 3 characters.", "error_recipe_name" )
            isValid = False
        if  len(data['description']) < 3:
            flash("You must provide description with at lease 3 characters.", "error_recipe_description" )
            isValid = False
        if  len(data['instructions']) < 3:
            flash("You must provide instructions with at lease 3 characters.", "error_recipe_instructions" )
            isValid = False
        if data['date_made'] == "":
            flash("Please provide a valid date.", "error_recipe_date_made")
            isValid = False
        if data['under30mins'] == "":
            flash("You must selete yes or no.", "error_recipe_under30mins")
            isValid = False

        return isValid