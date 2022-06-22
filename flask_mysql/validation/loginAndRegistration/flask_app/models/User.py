from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re    # the regex module    

class User:
    def __init__( self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_login(data):
        isValid = True
        if data['email'] == "":
            flash("Please provide your email.", "error_email" )
            isValid = False
        if data['password'] == "":
            flash("Please provide your password.", "error_password")
            isValid = False
        return isValid

    @staticmethod
    def validate_session():
        if "id" in session:
            return True
        else:
            flash("You must be logged in to see the dashboard.", "error_login")
            return False


    @staticmethod
    def validate_registration(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$')
        #print("validate_registration(data)", data)
        print("---Data-----::: ",data)
        isValid = True
        if data['first_name'] == "":
            flash("You must provide your first name.", "error_register_first_name" )
            isValid = False
        if data['last_name'] == "":
            flash("You must provide your last name.", "error_register_last_name" )
            isValid = False
        if data['email'] == "":
            flash("You must provide your email.", "error_register_email" )
            isValid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Please provide a valid email.", "error_register_email")
            isValid = False
        elif User.getAllUsers(data):
            flash("This email is taken.", "error_register_email")
            isValid = False
        if data['password'] == "":
            flash("You must provide a password.", "error_register_password")
            isValid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("Please provide a password with minimum of six characters, at least one uppercase letter, one lowercase letter and one number:", "error_register_password")
            isValid = False
        if data['Confirm_password'] != data['password']:
            flash("Your password confirmation doesn't match.", "error_register_password_confirmation")
            isValid = False
        if len(data['password']) < 5:
            flash("Password must be at least 6 characters long.", "error_register_password")
            isValid = False

        return isValid

    @classmethod
    def addNewUser(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) "
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"
        newUserID = connectToMySQL('users_schema').query_db(query, data)
        
        return newUserID

    @classmethod
    def getUser(cls, data):
        query = "select * FROM users "
        query += "WHERE email=%(email)s;"
        results = connectToMySQL('users_schema').query_db(query, data)
        print(results)
        if len(results) > 0:
            return cls(results[0])
        else:
            return None

    @classmethod
    def getAllUsers(cls, data):
        print("data from getAllUsers query ----", data)
        query = "select * FROM users where email = %(email)s"
        results = connectToMySQL('users_schema').query_db(query, data)
        print("results from getAllUsers query ----", results)
        if results:
            return True
        else:
            return False