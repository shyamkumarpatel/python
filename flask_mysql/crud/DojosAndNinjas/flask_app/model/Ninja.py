from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    def __init__( self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT id, first_name, last_name, age, created_at, updated_at, dojo_id FROM ninjas;"
        
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query)
        
        Ninjas = []
        
        for Ninja in results:
            Ninjas.append( cls(Ninja) )
        return Ninjas

    @classmethod
    def addNewNinja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) "
        query += "VALUES ( %(first_name)s,  %(last_name)s, %(age)s, %(dojo_id)s );"
        newNinjaID = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        
        return newNinjaID

    @classmethod
    def getNinja(cls, data):
        query = "select  id, first_name, last_name, age, created_at, updated_at, dojo_id FROM ninjas "
        query += "WHERE id = %(id)s ;"
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        return cls(results[0])
