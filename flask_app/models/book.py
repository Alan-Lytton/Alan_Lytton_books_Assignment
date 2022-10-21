from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the table from our database
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM books WHERE id = %(book_id)s;"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def add_new(cls,data):
        query = 'INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(pages)s, now(),now());'
        return connectToMySQL('books_schema').query_db(query, data)
