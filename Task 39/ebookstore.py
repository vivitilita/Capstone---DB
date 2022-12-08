# import books_database.py file to apply to the ebookstore program
import books_database

# This is a simple program that can be used by a bookstore clerk. 
# The program should allow the clerk to:
# - add new books to the database
# - update book information
# - delete books from the database
# - search the database to find a specific book.



# Welcome message
print('''              WELCOME TO EBOOKSTORE

             .--.           .---.        .-.
         .---|--|   .-.     | B |  .---. |~|    .--.
      .--|===|Sq|---|_|--.__| O |--|:::| |~|-==-|==|---.
      |  | A |li|===| |~~|  | O |--|   |_|~| Py |  |___|-.
      |  | r |te|===| |==|  | K |  |:::|=| | th |GB|---|=|
      |  | t | 3|   |_|__|  | S |__|   | | | on |  |___| |
      |~~|===|--|===|~|~~|  |~~~|--|:::|=|~|----|==|---|=|
      ^--^---'--^---^-^--^--^---'--^---^-^-^-==-^--^---^-''')

# Menu options
menu_options = ('''\n~~~~~~ MENU OPTIONS ~~~~~~\n
1 --> Enter Book
2 --> Update Book
3 --> Delete Book
4 --> Search Books
0 --> Exit
---------------------
Enter your selection: ''')

# the given books from records variable were added individually through the menu options
records = [(3001, "A Tale of Two Cities", "Charles Dickens", 30), 
(3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
(3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
(3004, "The Lord of the Rings", "J.R.R. Tolkien", 37),
(3005, "Alice in Wonderland", "Lewis Caroll", 12)]

# Creating and/or connecting to the database
def menu():
    books_db = books_database.connect_db()
    books_database.create_table(books_db)


# menu functionality by user input
    while (user_input := input(menu_options)) != '5':
        print(user_input)
        if user_input == '0':
            print('Thank you for using the ebookstore. Bye!\n')
            books_db.close() # closing the database
            exit()

        elif user_input == '1':
            enter_NewBook(books_db) # adding a new book
            books_db.commit()
        
        elif user_input == '2':
            update_Book(books_db) # updating a book
            books_db.commit()

        elif user_input == '3':
            delete_Book(books_db) # deleting a book
            books_db.commit()

        elif user_input =='4':
            option = input('Enter 1 to search by Title or Author or enter 2 to see All books: ').upper()
            if option == '1':
                see_by_Book(books_db) # displays the chosen book
            else:
                see_AllBooks(books_db) # displays all books
        
        else:
            print('Invalid input. Try again!') # message for invalid input


# Entering a new book
def enter_NewBook(books_db):
    title = input('Enter Title: ')
    author = input('Enter Author: ')
    qty = int(input('Enter Quantity: '))
    id = int(input('Enter id: '))
    books_database.enter_book(books_db, title, author, qty, id)
    books_db.commit()
    print('New book saved.\n')

# Updating a book
def update_Book(books_db):
    title = input('Enter Title: ')
    author = input('Enter Author: ')
    qty = int(input('Enter Quantity: '))
    id = int(input('Enter id: '))
    books_database.book_update(books_db, title, author, qty, id)
    books_db.commit()
    print('Book updated.\n')

# Deleting a book
def delete_Book(books_db):
    id = input('Enter Book id: ')
    books_database.book_delete(books_db, id)
    books_db.commit()
    print('Book deleted.\n')

# Displaying all books
def see_AllBooks(books_db):
    books = books_database.list_all_books(books_db)
    for book in books:
        print(f'''Book id: {book[0]} | Qty: {book[3]}
  Title: {book[1]} (by {book[2]}) \n''')
        books_db.commit()

# Searching books
def see_by_Book(books_db):
    check = input('Search Book by Title/Author: ').upper()
    get = books_database.book_search(books_db, check, check)
    for book in get:
        print(f'''Book id: {book[0]} | Qty: {book[3]}
  Title: {book[1]} (by {book[2]}) \n''')
        books_db.commit()

menu() # returns menu options
