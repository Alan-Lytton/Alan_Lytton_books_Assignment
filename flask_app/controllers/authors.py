from flask import render_template, request, redirect, session
from flask_app.models.author import Author  #change this import line based on your extra .py file for generating OOP instances
from flask_app import app


@app.route("/authors")     # lines 6 through 11 can be changed depending on what we need server.py to do.
def r_get_all_authors():
    # call the get all classmethod to get all books
    authors = Author.get_all()
    return render_template("authors.html", authors = authors)

@app.route('/authors/add', methods=['POST'])
def f_add_author():
    data = {
        'author_name':request.form['author']
    }
    Author.add_new(data)
    return redirect('/authors')