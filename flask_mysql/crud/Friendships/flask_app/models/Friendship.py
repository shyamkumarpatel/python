from flask_app.config.mysqlconnection import connectToMySQL

class Friendship:
    def __init__( self , data):
        self.id = data['id']
        self.users_id = data['users_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT id, users_id, friend_id, created_at, updated_at FROM friendships;"
        results = connectToMySQL('friendships_schema').query_db(query)
        #print(results)
        Friendships = []
        for friendship in results:
            Friendships.append( cls(friendship) )
        return Friendships

    @classmethod
    def addNewFriendship(cls, data):
        query = "INSERT INTO friendships (users_id, friend_id)"
        query += "VALUES ( %(user_id)s, %(friend_id)s );"
        newUserID = connectToMySQL('friendships_schema').query_db(query, data)
        
        return newUserID