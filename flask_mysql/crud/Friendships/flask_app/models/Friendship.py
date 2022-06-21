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

    @classmethod
    def getAllFriendships(cls, data):
        query = "select  * "
        query += "from users INNER JOIN friendships on users.id = friendships.users_id "
        query += "WHERE users.id = %(id)s ;"
        results = connectToMySQL('friendships_schema').query_db(query, data)
        # print(results)
        # one_user = cls(results[0])

        # for row in results:
        #     ninja_info = {
        #         'id' : row['id'],
        #         'first_name' : row['first_name'],
        #         'last_name' : row['last_name'],
        #         'age' : row['age'],
        #         'created_at' : row['created_at'],
        #         'updated_at' : row['updated_at'],
        #         'dojo_id' : row['dojo_id']
        #     }

        #     one_user.friendships.append(Friendship(ninja_info))

        return results