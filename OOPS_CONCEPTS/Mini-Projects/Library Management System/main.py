import json


class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book was not borrowed.")

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(
            f"ID: {self.book_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Status: {status}"
        )


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists.")
                return

        self.books.append(Book(book_id, title, author))
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            book.display()

    def search_book(self):
        title = input("Enter title to search: ").lower()

        found = False

        for book in self.books:
            if title in book.title.lower():
                book.display()
                found = True

        if not found:
            print("Book not found.")

    def borrow_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                book.borrow()
                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                return

        print("Book not found.")

    def save_books(self):
        data = []

        for book in self.books:
            data.append({
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "available": book.available
            })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)

                for item in data:
                    self.books.append(
                        Book(
                            item["book_id"],
                            item["title"],
                            item["author"],
                            item["available"]
                        )
                    )

        except FileNotFoundError:
            pass


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.borrow_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.save_books()
        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid choice.")