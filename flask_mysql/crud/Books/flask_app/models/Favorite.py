from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.Author import Author
from flask_app.models.Book import Book

class Favorite:
    def __init__( self , data):
        self.bookID = data['bookID']
        self.authorID = data['authorID']

    @classmethod
    def addFavorite(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) "
        query += "VALUES ( %(user_id)s,  %(book_id)s );"
        lastInsertedRowID = connectToMySQL('books_schema').query_db(query, data)
        
        return lastInsertedRowID

    @classmethod
    def get_fav_books(cls, data):
        query = "SELECT	b.* "
        query += "FROM favorites f "
        query += "LEFT JOIN authors a on f.user_id = a.id "
        query += "LEFT JOIN books b on f.book_id = b.id "
        query += "WHERE f.user_id = %(id)s ;"
        results = connectToMySQL('books_schema').query_db(query, data)
        Books = []
        
        for book in results:
            Books.append( Book(book) )
        
        #print(" Book Objects ---> ",Books)
        return Books

    @classmethod
    def get_fav_authors(cls, data):
        query = "SELECT a.* "
        query += "FROM favorites f "
        query += "LEFT JOIN authors a on f.user_id = a.id "
        query += "LEFT JOIN books b on f.book_id = b.id "
        query += "WHERE f.book_id = %(id)s ;"
        results = connectToMySQL('books_schema').query_db(query, data)
        Authors = []
        
        for author in results:
            Authors.append( Author(author) )
        
        #print(" Book Objects ---> ",Books)
        return Authors