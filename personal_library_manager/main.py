import json
import os

LIBRARY_FILE = "library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    library.append({
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    })
    save_library(library)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(f"Book '{title}' removed successfully!")
            return
    print("Book not found!")

def update_book(library):
    title = input("Enter the title of the book to update: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            print(f"Updating '{title}'. Press Enter to keep the current value.")
            new_title = input(f"New title ({book['title']}): ").strip() or book["title"]
            new_author = input(f"New author ({book['author']}): ").strip() or book["author"]
            new_year = input(f"New year ({book['year']}): ").strip() or book["year"]
            new_genre = input(f"New genre ({book['genre']}): ").strip() or book["genre"]

            book["title"] = new_title
            book["author"] = new_author
            book["year"] = int(new_year)
            book["genre"] = new_genre
            save_library(library)
            print("Book updated successfully!")
            return
    print("Book not found!")

def update_read_status(library):
    title = input("Enter the title of the book to update read status: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            read_status = input(f"Mark '{title}' as Read? (yes/no): ").strip().lower() == "yes"
            book["read"] = read_status
            save_library(library)
            print(f"Read status updated for '{title}'!")
            return
    print("Book not found!")

def search_books(library):
    query = input("Enter book title or author to search: ").strip().lower()
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    if results:
        print("\nSearch Results:")
        display_books(results)
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("No books found in the library.")
        return
    print("\nLibrary Collection:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} [{status}]")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({read_percentage:.2f}%)")

def main():
    library = load_library()
    while True:
        print("\n📚 Personal Library Manager 📚")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Update Book Details")
        print("4. Update Read Status")
        print("5. Search for a Book")
        print("6. Display All Books")
        print("7. Display Statistics")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            update_book(library)
        elif choice == "4":
            update_read_status(library)
        elif choice == "5":
            search_books(library)
        elif choice == "6":
            display_books(library)
        elif choice == "7":
            display_statistics(library)
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()