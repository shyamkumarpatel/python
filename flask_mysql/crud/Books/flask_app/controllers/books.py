from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.Book import Book
from flask_app.models.Author import Author

@app.route("/books")
def add_book():
    Books = Book.get_all()
    return render_template("books.html", all_books = Books)


@app.route("/books/<int:id>")
def getBookInfo(id):
    data={'id':id}
    book_info = Book.getBook(data)
    author_info = Author.get_all()
    return render_template("book_show.html", Book_Info = book_info, authors = author_info)


@app.route("/newBooks", methods=["POST"])
def add_new_book():
    print(request.form)
    last_id_inserted = Book.addNewBook(request.form)
    print(last_id_inserted)
    return redirect("/books")