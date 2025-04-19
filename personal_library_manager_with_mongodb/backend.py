# auth.py
from pymongo import MongoClient
from dotenv import load_dotenv
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri, tlsAllowInvalidCertificates=True)
db = client.library
user_collection = db.users
bk_collection = db.books
ph = PasswordHasher()

# auth 
def register_user(username: str, email: str, password: str) -> str|None:
    if user_collection.find_one({"email": email}):
        return "❌ Email already registered."

    hashed_pw = ph.hash(password)
    user_collection.insert_one({
        "username": username,
        "email": email,
        "password": hashed_pw,
    })
    return login_user()

def login_user(email: str, password: str) -> str|None:
    user = user_collection.find_one({"email": email})
    if not user:
        return "❌ Email not found."

    try:
        if ph.verify(user["password"], password):
            return user["_id"]
    except VerifyMismatchError:
        return None

    return None


# library 

def add_book(title: str,author: str,genre: str,status: str):
    try:
        book = {
            "title": title.strip(),
            "author": author.strip(),
            "genre": genre.strip(),
            "status": status
        }
        bk_collection.insert_one(book)
        return f"📖 Book '{title}' added!"
    except Exception as e:
        return f"❌ Error adding book '{title}': {e}"
    
# def remove_book():
#     try:
#         books = bk_collection.find(book_to_remove)
#         if not books:
#             return "No books to remove."
#         else:
#             titles = [book["title"] for book in books]
#             bk_collection.delete_one({"title": book_to_remove})
#             return f"Deleted '{book_to_remove}' from your library."
#     except Exception as e:
#         return f"❌ Error removing book!"
