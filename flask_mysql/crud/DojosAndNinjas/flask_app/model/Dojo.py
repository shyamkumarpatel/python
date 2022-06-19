from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model.Ninja import Ninja
class Dojo:
    def __init__( self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT id, name, created_at, updated_at FROM dojos;"
        
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query)
        
        Dojos = []
        
        for Dojo in results:
            Dojos.append( cls(Dojo) )
        return Dojos

    @classmethod
    def addNewDojo(cls, data):
        query = "INSERT INTO dojos (name)"
        query += "VALUES ( %(name)s );"
        newDojoID = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        
        return newDojoID

    @classmethod
    def getDojo(cls, data):
        query = "select id, name, created_at, updated_at FROM dojos "
        query += "WHERE id = %(id)s ;"
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def getDojoNinjas(cls, data):
        query = "select  * "
        query += "FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id "
        query += "WHERE dojos.id = %(id)s ;"
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        print(results)
        one_dojo = cls(results[0])

        for row in results:
            ninja_info = {
                'id' : row['id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at'],
                'dojo_id' : row['dojo_id']
            }

            one_dojo.ninjas.append(Ninja(ninja_info))

        return one_dojo