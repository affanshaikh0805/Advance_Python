class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("\nBook ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)


class Patron:

    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print("\nPatron ID:", self.patron_id)
        print("Name:", self.name)
        print("Borrowed Books:", len(self.borrowed_books))


class Library:

    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books:
                book.display()

    def borrow_book(self, book_id, patron_id):

        book_found = None
        patron_found = None

        # Search for the book
        for book in self.books:
            if book.book_id == book_id:
                book_found = book
                break

        # Search for the patron
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                patron_found = patron
                break

        if book_found is None:
            print("Book not found.")
            return

        if patron_found is None:
            print("Patron not found.")
            return

        if book_found.available:
            book_found.available = False
            patron_found.borrowed_books.append(book_found)
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self, book_id, patron_id):

        patron_found = None

        # Search for patron
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                patron_found = patron
                break

        if patron_found is None:
            print("Patron not found.")
            return

        # Search in borrowed books
        for book in patron_found.borrowed_books:
            if book.book_id == book_id:
                book.available = True
                patron_found.borrowed_books.remove(book)
                print("Book returned successfully.")
                return

        print("This patron has not borrowed this book.")


# ---------------- MAIN PROGRAM ----------------

library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == 2:

        patron_id = int(input("Enter Patron ID: "))
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == 3:

        book_id = int(input("Enter Book ID: "))
        patron_id = int(input("Enter Patron ID: "))

        library.borrow_book(book_id, patron_id)

    elif choice == 4:

        book_id = int(input("Enter Book ID: "))
        patron_id = int(input("Enter Patron ID: "))

        library.return_book(book_id, patron_id)

    elif choice == 5:

        library.display_books()

    elif choice == 6:

        print("Thank you for using the Library Management System.")
        break

    else:

        print("Invalid choice.")