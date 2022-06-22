from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__( self , data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT id, title, num_of_pages, created_at, updated_at FROM books;"
        
        results = connectToMySQL('books_schema').query_db(query)
        
        Books = []
        
        for book in results:
            Books.append( cls(book) )
        return Books

    @classmethod
    def addNewBook(cls, data):
        query = "INSERT INTO books (title, num_of_pages) "
        query += "VALUES ( %(title)s,  %(num_of_pages)s );"
        lastInsertedRowID = connectToMySQL('books_schema').query_db(query, data)
        
        return lastInsertedRowID

    @classmethod
    def getBook(cls, data):
        query = "select  id, title, num_of_pages, created_at, updated_at FROM books "
        query += "WHERE id = %(id)s ;"
        results = connectToMySQL('books_schema').query_db(query, data)
        return cls(results[0])
