from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import Book, Author
class Favorites:
    def __init__( self , data):
        self.bookID = data['bookID']
        self.authorID = data['authorID']
        self.authors = []
        self.books = []

    @classmethod
    def get_authors(cls):
        query = "SELECT id, name, created_at, updated_at FROM authors;"
        
        results = connectToMySQL('books_schema').query_db(query)
        
        Authors = []
        
        for author in results:
            Authors.append( cls(author) )
        return Authors

    @classmethod
    def get_books(cls):
        query = "SELECT id, name, created_at, updated_at FROM authors;"
        
        results = connectToMySQL('books_schema').query_db(query)
        
        Authors = []
        
        for author in results:
            Authors.append( cls(author) )
        return Authors