from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.Author import Author
from flask_app.models.Book import Book

@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def getAuthors():
    Authors = Author.get_all()
    return render_template("index.html", all_Authors = Authors)

@app.route("/authors/<int:id>")
def getNinjaInfo(id):
    data={'id':id}
    author_info = Author.getAuthor(data)
    book_info = Book.get_all()
    return render_template("author_show.html", Author_Info = author_info, books = book_info)

@app.route("/newauthor", methods=["POST"])
def add_new_dojo():
    last_id_inserted = Author.addNewAuthor(request.form)
    return redirect("/authors")