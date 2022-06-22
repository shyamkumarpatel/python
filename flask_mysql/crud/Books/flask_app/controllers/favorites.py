from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.Book import Book
from flask_app.models.Author import Author
from flask_app.models.Favorite import Favorite


@app.route("/newFavBook", methods=["POST"])
def add_new_Fav_book():
    print("Form Data ----> ", request.form)
    Favorite.addFavorite(request.form)
    return redirect(f"/authors/{request.form['user_id']}")

@app.route("/newFavAuthor", methods=["POST"])
def add_new_Fav_Author():
    print("Form Data ----> ", request.form)
    Favorite.addFavorite(request.form)
    return redirect(f"/books/{request.form['book_id']}")