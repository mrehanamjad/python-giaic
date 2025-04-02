
AllBooks = []

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    publication_year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    reading_status_inp = input("Enter the reading status (yes/no): ")
    reading_status = False
    if reading_status_inp == 'yes':
        reading_status = True
    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "reading_status": reading_status,
    }
    AllBooks.append(book)
    print(f"Book '{title}' added successfully.")

def remove_book():
    global AllBooks
    title = input("Enter the title of the book to remove: ")
    AllBooks = [d for d in AllBooks if d.get('title') != title]
    print(f"Book '{title}' removed successfully.".center(10,"*"))

def display_books():
    print("All Books:")

    for book in AllBooks:
        print(f"Title: {book['title']}, Author: {book['author']}, Publication Year: {book['publication_year']}, Genre: {book['genre']}, Reading Status: {book['reading_status']}")

def main():
    print("Welcome to your Personal Library Manager!")
    print("Options:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display all books")
    print("4. Exit")
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_book()
        elif choice == "2":   
            remove_book()
        elif choice == "3":
            display_books()
        elif choice == "4":
            print("Thank you for using the Personal Library Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

