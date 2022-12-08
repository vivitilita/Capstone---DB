import sqlite3 # import package for database interaction

# Assign variables

# create table if it does not exist one
books_table = '''CREATE TABLE IF NOT EXISTS Books( id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)'''

# add a book
add_book = '''INSERT INTO Books(Title, Author, Qty, id) VALUES(?,?,?,?)'''

# update a book
update_book = '''UPDATE Books SET Title= ?, Author= ?, Qty= ? WHERE  id= ?'''

# delete a book
delete_book = '''DELETE FROM Books WHERE id= ?'''

# search books
search_book = '''SELECT * FROM Books WHERE Title LIKE ? OR Author LIKE ?'''

# list all books
all_books = '''SELECT * FROM Books'''

# Creating function for ebookstore usability:

# connecting to ebookstore database
def connect_db(): 
    return sqlite3.connect('ebookstore.db')

# creating a table
def create_table(books_db):
    with books_db:
        books_db.execute(books_table)

# entering a new book
def enter_book(books_db, Title, Author, Qty, id):
    with books_db:
        books_db.execute(add_book, (Title, Author, Qty, id))

# updating a book
def book_update(books_db, Title, Author, Qty, id):
    with books_db:
        books_db.execute(update_book, (Title, Author, Qty, id))

# deleting a book
def book_delete(books_db, id):
    with books_db:
        books_db.execute(delete_book, (id,))

# searching books
def book_search(books_db, Title, Author):
    with books_db:
        return books_db.execute(search_book, (Title, Author)).fetchall()

# listing all books
def list_all_books(books_db):
    with books_db:
        return books_db.execute(all_books).fetchall()