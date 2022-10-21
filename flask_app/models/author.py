
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        # adjust the "FROM" target to be the required table
        query = "SELECT * FROM users;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(author_id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_new(cls,data):
        query = "INSERT INTO users (name, created_at, updated_at) VALUES (%(author_name)s, now(), now());"
        return connectToMySQL('books_schema').query_db(query,data)

