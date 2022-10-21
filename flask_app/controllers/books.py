from flask import render_template, request, redirect, session
from flask_app.models.book import Book  #change this import line based on your extra .py file for generating OOP instances
from flask_app import app


@app.route("/books")     # lines 6 through 11 can be changed depending on what we need server.py to do.
def r_get_all_books():
    # call the get all classmethod to get all books
    books = Book.get_all()
    return render_template("books.html", books = books)

@app.route('/books/add', methods = ['POST'])
def f_add_new_book():
    data = {
        'title':request.form['title'],
        'pages':request.form['pages']
    }
    Book.add_new(data)
    return redirect('/books')