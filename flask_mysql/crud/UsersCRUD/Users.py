from mysqlconnection import connectToMySQL
class User:
    def __init__( self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users;"
        
        results = connectToMySQL('users_schema').query_db(query)
        
        Users = []
        
        for User in results:
            Users.append( cls(User) )
        return Users

    @classmethod
    def addNewUser(cls, data):
        query = "INSERT INTO users (first_name, last_name, email)"
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email)s );"
        newUserID = connectToMySQL('users_schema').query_db(query, data)
        
        print(newUserID)
        return newUserID

    @classmethod
    def getUser(cls, data):
        query = "select id, first_name, last_name, email, created_at, updated_at FROM users;"
        query += "WHERE id = %(id)s ;"
        print("\n---------------------------------------",
                query,"\n",
                data,"\n------------------------------------------------------")
        results = connectToMySQL('users_schema').query_db(query, data)
        print("---- User Info Fetched ----------------------\n",results,"\n------------------------------------------------------")
        return results
