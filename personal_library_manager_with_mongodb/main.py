import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri,tlsAllowInvalidCertificates=True)
db = client.library  # Assuming you have a 'library' database
collection = db.books  # A collection for books

# App title
st.title("📚 Personal Library Manager")
st.markdown("----")

# Menu - Using Radio button instead of dropdown (selectbox)
menu = [
    "Add a Book",
    "Remove a Book",
    "Update Book Details",
    "Update Read Status",
    "Search for a Book",
    "Display All Books",
    "Display Statistics"
]

choice = st.sidebar.radio("Menu", menu)

# 1. Add Book
if choice == "Add a Book":
    st.header("➕ Add a Book")
    with st.form("add_form", clear_on_submit=True):
        title = st.text_input("Title")
        author = st.text_input("Author")
        genre = st.text_input("Genre")
        status = st.selectbox("Status", ["Unread", "Read"])
        submit = st.form_submit_button("Add Book")

        if submit:
            if title.strip() and author.strip():
                book = {
                    "title": title.strip(),
                    "author": author.strip(),
                    "genre": genre.strip(),
                    "status": status
                }
                collection.insert_one(book)
                st.success(f"📖 Book '{title}' added!")
            else:
                st.warning("Title and Author are required.")

# 2. Remove Book
elif choice == "Remove a Book":
    st.header("❌ Remove a Book")
    books = collection.find()
    if not books:
        st.info("No books to remove.")
    else:
        titles = [book["title"] for book in books]
        book_to_remove = st.selectbox("Select Book", titles)
        if st.button("Remove"):
            collection.delete_one({"title": book_to_remove})
            st.success(f"Deleted '{book_to_remove}' from your library.")
            st.experimental_rerun()

# 3. Update Book Details
elif choice == "Update Book Details":
    st.header("📝 Update Book Details")
    books = collection.find()
    if not books:
        st.info("No books to update.")
    else:
        titles = [book["title"] for book in books]
        selected_title = st.selectbox("Select Book", titles)
        book = collection.find_one({"title": selected_title})

        if book:
            new_title = st.text_input("Title", book["title"])
            new_author = st.text_input("Author", book["author"])
            new_genre = st.text_input("Genre", book["genre"])

            if st.button("Update"):
                collection.update_one(
                    {"title": selected_title},
                    {"$set": {"title": new_title, "author": new_author, "genre": new_genre}}
                )
                st.success("Book details updated successfully.")
                st.experimental_rerun()

# 4. Update Read Status
elif choice == "Update Read Status":
    st.header("✅ Update Read Status")
    books = collection.find()
    if not books:
        st.info("No books to update.")
    else:
        titles = [book["title"] for book in books]
        selected_title = st.selectbox("Select Book", titles)
        new_status = st.radio("New Status", ["Unread", "Read"])
        if st.button("Update Status"):
            collection.update_one(
                {"title": selected_title},
                {"$set": {"status": new_status}}
            )
            st.success(f"Updated status of '{selected_title}' to {new_status}.")
            st.experimental_rerun()

# 5. Search for a Book
elif choice == "Search for a Book":
    st.header("🔍 Search for a Book")
    query = st.text_input("Search by Title or Author")
    if query:
        results = collection.find({
            "$or": [
                {"title": {"$regex": query, "$options": "i"}},
                {"author": {"$regex": query, "$options": "i"}}
            ]
        })
        if results:
            for book in results:
                st.markdown(f"**{book['title']}** by *{book['author']}* ({book['genre']}) - {book['status']}")
        else:
            st.warning("No matching books found.")

# 6. Display All Books
elif choice == "Display All Books":
    st.header("📋 All Books")
    books = collection.find()
    if not books:
        st.info("No books in your library.")
    else:
        books_data = [
            {
                "Title": book["title"],
                "Author": book["author"],
                "Genre": book["genre"],
                "Status": book["status"]
            }
            for book in books
        ]
        st.table(books_data)

# 7. Display Statistics
elif choice == "Display Statistics":
    st.header("📊 Library Statistics")

    books = list(collection.find())
    total_books = len(books)
    read_books = len([book for book in books if book["status"] == "Read"])
    unread_books = total_books - read_books
    genres = set(book["genre"] for book in books if book["genre"])

    # Display overall statistics using st.metric
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="📚 Total Books", value=total_books)
    with col2:
        st.metric(label="✅ Read Books", value=read_books)
    with col3:
        st.metric(label="📖 Unread Books", value=unread_books)

    # Create a bar chart for read/unread books
    if total_books > 0:
        data = {"Read": read_books, "Unread": unread_books}
        st.bar_chart(data)

    # Display genres in a nice format with count
    if genres:
        st.subheader("🏷️ Genres")
        genre_counts = {genre: sum(1 for book in books if book["genre"] == genre) for genre in genres}
        for genre, count in genre_counts.items():
            st.markdown(f"**{genre}**: {count} book(s)")

    else:
        st.warning("No genres available.")
