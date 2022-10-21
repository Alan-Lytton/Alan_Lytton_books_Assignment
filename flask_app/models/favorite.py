from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Favorite:
    def __init__( self , data ):
        self.books_id = data['books.id']
        self.title = data['books.title']
        self.num_of_pages = data['books.num_of_pages']
        self.users_id = data['users.id']
        self.name = data['users.name']
        self.fav_user_id = data['fav_user_id']
        self.fav_book_id = data['fav_book_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM favorites;"
        results = connectToMySQL('books_schema').query_db(query)
        favorites = []
        for favorite in results:
            favorites.append( cls(favorite) )
        return favorites

    @classmethod
    def get_one(cls,data):
        query = "SELECT books.id AS book_id, books.title, books.num_of_pages, users.id AS user_id, users.name, favorites.user_id AS fav_user_id, favorites.book_id AS fav_book_id  FROM users JOIN favorites ON users.id = favorites.user_id JOIN books ON favorites.book_id = books.id WHERE users.id = %(author_id)s;"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def new_fav_book(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def get_one_book(cls,data):
        query = "SELECT books.id AS book_id, books.title, books.num_of_pages, users.id AS user_id, users.name, favorites.user_id AS fav_user_id, favorites.book_id AS fav_book_id  FROM users JOIN favorites ON users.id = favorites.user_id JOIN books ON favorites.book_id = books.id WHERE books.id = %(book_id)s ;"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def new_author_fav(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db(query, data)