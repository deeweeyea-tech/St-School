class Library:
    def __init__(self):
        self.books = []        # list of all book titles
        self.issued = {}       # dictionary: book title -> student name

    def add_book(self, title):
        self.books.append(title)
        print("Book added successfully.")

    def issue_book(self, title, student_name):
        if title not in self.books:
            print("Book not found in library.")
        elif title in self.issued:
            print("Book is already issued.")
        else:
            self.issued[title] = student_name
            print("Book issued to", student_name)

    def return_book(self, title):
        if title in self.issued:
            del self.issued[title]
            print("Book returned successfully.")
        else:
            print("This book was not issued.")

    def display_available_books(self):
        print("Available Books:")
        found = False
        for book in self.books:
            if book not in self.issued:
                print("-", book)
                found = True
        if not found:
            print("No books available.")


library = Library()

# Menu-driven program
while True:
    print()
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        library.add_book(title)
    elif choice == 2:
        title = input("Enter book title: ")
        name = input("Enter student name: ")
        library.issue_book(title, name)
    elif choice == 3:
        title = input("Enter book title: ")
        library.return_book(title)
    elif choice == 4:
        library.display_available_books()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")