from flask_app.config.mysqlconnection import connectToMySQL
class Favorites:
    def __init__( self , data):
        self.bookID = data['bookID']
        self.authorID = data['authorID']

    @classmethod
    def get_all(cls):
        query = "SELECT id, name, created_at, updated_at FROM authors;"
        
        results = connectToMySQL('books_schema').query_db(query)
        
        Authors = []
        
        for author in results:
            Authors.append( cls(author) )
        return Authors