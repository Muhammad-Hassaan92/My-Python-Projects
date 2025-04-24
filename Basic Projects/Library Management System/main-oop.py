# Library Management System

# Task Description

# Create a simple library management system using Python. The system should allow users to perform basic operations such as adding, removing, and searching for books.

# Requirements

# 1. Use Python 3.x
# 2. Use a dictionary to store book data (title, author, publication year, status)
# 3. Implement the following features:

# Features

# 1. Add Book
#     - Prompt user for book title, author, and publication year
#     - Add book to library dictionary with status "available"

# 2. Remove Book
#     - Prompt user for book title
#     - Remove book from library dictionary if found

# 3. Search Book
#     - Prompt user for book title or author
#     - Display book details if found

# 4. Borrow Book
#     - Prompt user for book title
#     - Update book status to "borrowed" if available

# 5. Return Book
#     - Prompt user for book title
#     - Update book status to "available" if borrowed

# 6. Display All Books
#     - Display list of all books in library

# Evaluation Criteria

# 1. Correct implementation of library management system features
# 2. Proper use of Python dictionary to store book data
# 3. Clean and readable code
# 4. User-friendly interface
# 5. Error handling for invalid user inputs

# Time Estimate

# Approximately 2 hours to complete task.

# Tips

# - Use functions to organize code and reduce repetition.
# - Use descriptive variable names.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = 'available'

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.status}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the publication year: ")
        
        if title not in self.books:
            self.books[title] = Book(title, author, year)
            print(f"Book '{title}' added successfully.")
        else:
            print(f"Book '{title}' already exists in the library.")

    def remove_book(self):
        title = input("Enter the book title to remove: ")
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found in the library.")

    def search_book(self):
        search_query = input("Enter book title or author to search: ").lower()
        found = False
        for book in self.books.values():
            if search_query in book.title.lower() or search_query in book.author.lower():
                print(book)
                found = True
        if not found:
            print(f"No books found matching '{search_query}'.")

    def borrow_book(self):
        title = input("Enter the book title to borrow: ")
        if title in self.books:
            book = self.books[title]
            if book.status == 'available':
                book.status = 'borrowed'
                print(f"You have borrowed '{title}'.")
            else:
                print(f"Sorry, the book '{title}' is currently borrowed.")
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self):
        title = input("Enter the book title to return: ")
        if title in self.books:
            book = self.books[title]
            if book.status == 'borrowed':
                book.status = 'available'
                print(f"Book '{title}' returned successfully.")
            else:
                print(f"Book '{title}' was not borrowed.")
        else:
            print(f"Book '{title}' not found in the library.")

    def display_books(self):
        if self.books:
            print("\nLibrary Collection:")
            for book in self.books.values():
                print(book)
        else:
            print("The library is empty.")


# Main program to interact with the library
def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Display All Books")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.remove_book()
        elif choice == '3':
            library.search_book()
        elif choice == '4':
            library.borrow_book()
        elif choice == '5':
            library.return_book()
        elif choice == '6':
            library.display_books()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
