from flask import render_template, request, redirect, session, url_for
from flask_app.models.favorite import Favorite  #change this import line based on your extra .py file for generating OOP instances
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app



@app.route('/authors/show/<int:id>')
def r_show_one(id):
    author_id = id
    data = {
        'author_id': author_id
    }
    author = Author.get_one(data)
    favorites = Favorite.get_one(data)
    books = Book.get_all()
    return render_template('author_show.html', author = author, favorites = favorites, books = books)

@app.route('/authors/show/add', methods = ['POST'])
def f_add_new_fav():
    data = {
        'book_id': request.form.get('new_book'),
        'user_id': request.form ['user_id']    
    }
    Favorite.new_fav_book(data)
    return redirect(url_for('r_show_one', id = data['user_id']))

@app.route('/books/show/<int:book_id>')
def r_show_one_book(book_id):
    data = {
        'book_id':book_id
    }
    book = Book.get_one(data)
    authors = Author.get_all()
    favorites = Favorite.get_one_book(data)
    return render_template('book_show.html', book=book, authors=authors, favorites=favorites)

@app.route('/books/show/add', methods = ['POST'])
def f_add_fav_author():
    data = {
        'book_id': request.form['book_id'],
        'user_id': request.form.get('new_author_fav')
    }
    Favorite.new_author_fav(data)
    return redirect(url_for('r_show_one_book', book_id = data['book_id']))