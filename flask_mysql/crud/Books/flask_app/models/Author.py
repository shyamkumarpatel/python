from flask_app.config.mysqlconnection import connectToMySQL
class Author:
    def __init__( self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT id, name, created_at, updated_at FROM authors;"
        
        results = connectToMySQL('books_schema').query_db(query)
        
        Authors = []
        
        for author in results:
            Authors.append( cls(author) )
        return Authors

    @classmethod
    def addNewAuthor(cls, data):
        query = "INSERT INTO authors (name)"
        query += "VALUES ( %(name)s );"
        lastInsertedRowID = connectToMySQL('books_schema').query_db(query, data)
        
        return lastInsertedRowID

    @classmethod
    def getAuthor(cls, data):
        query = "select id, name, created_at, updated_at FROM authors "
        query += "WHERE id = %(id)s ;"
        results = connectToMySQL('books_schema').query_db(query, data)
        return cls(results[0])