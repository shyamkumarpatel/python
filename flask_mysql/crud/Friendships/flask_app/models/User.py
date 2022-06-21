from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.Friendship import Friendship

class User:
    def __init__( self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friendships = []

    @classmethod
    def get_all(cls):
        query = "SELECT id, first_name, last_name, created_at, updated_at FROM users;"
        results = connectToMySQL('friendships_schema').query_db(query)
        Users = []
        for user in results:
            Users.append( cls(user) )
        return Users

    @classmethod
    def addNewUser(cls, data):
        query = "INSERT INTO users (first_name, last_name)"
        query += "VALUES ( %(first_name)s, %(last_name)s );"
        newUserID = connectToMySQL('friendships_schema').query_db(query, data)
        
        return newUserID

    @classmethod
    def getUser(cls, data):
        query = "select id, first_name, last_name, created_at, updated_at FROM users "
        query += "WHERE id = %(id)s ;"
        results = connectToMySQL('friendships_schema').query_db(query, data)
        return cls(results[0])