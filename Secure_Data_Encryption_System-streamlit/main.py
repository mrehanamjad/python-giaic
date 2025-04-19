import sqlite3
import hashlib
import streamlit as st
from cryptography.fernet import Fernet
import base64
import uuid

conn = sqlite3.connect('sdes.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    encrypted_data TEXT NOT NULL,
    user_id TEXT NOT NULL
)
''')
conn.commit()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def generate_key(passkey: str) -> bytes:
    hashed_passkey = hashlib.sha256(passkey.encode()).digest()
    return base64.urlsafe_b64encode(hashed_passkey)

def encrypt_data(data: str, passkey: str) -> str:
    key = generate_key(passkey)
    fernet = Fernet(key)
    encrypt_data = fernet.encrypt(data.encode())
    return encrypt_data.decode()

def decrypt_data(encrypted_data: str, passkey: str) -> str:
    key = generate_key(passkey)
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted_data.encode())
        return decrypted.decode()
    except Exception:
        return "❌ Decryption failed! Incorrect passkey or corrupted data."

def insert_data(data: str, passkey: str, user_id: str) -> None:
    encrypted_data = encrypt_data(data, passkey)
    try:
        cursor.execute('''INSERT INTO data (encrypted_data, user_id) VALUES (?, ?);''', (encrypted_data, user_id))
        conn.commit()
        st.success("✅ Data inserted successfully!")
    except sqlite3.DatabaseError as e:
        st.error(f"❌ Database error occurred: {e}")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")

def get_encrypted_data(user_id: str) -> list:
    try:
        cursor.execute('''SELECT encrypted_data FROM data WHERE user_id = ?;''', (user_id,))
        data_entries = cursor.fetchall()
        return data_entries
    except sqlite3.DatabaseError as e:
        st.error(f"❌ Database error occurred: {e}")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")
    return []

def signup(name: str, email: str, password: str) -> None:
    try:
        _id = str(uuid.uuid4())
        hashed_password = hash_password(password)
        cursor.execute('''INSERT INTO users (id, name, email, password) VALUES (?, ?, ?, ?);''',
                       (_id, name, email, hashed_password))
        conn.commit()
        st.success("✅ User registered successfully!")
        st.session_state.authenticated = True
        st.session_state.user_data = {
            'id': _id,
            'name': name,
            'email': email,
            'password': hashed_password
        }
         # ✅ Debug: Print all users
        cursor.execute('SELECT * FROM users')
        st.write(cursor.fetchall())  
        # st.rerun()
    except sqlite3.IntegrityError:
        st.error("❌ Email already exists.")
    except sqlite3.DatabaseError as e:
        st.error(f"❌ Database error occurred: {e}")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")

def login(email: str, password: str) -> bool:
    try:
        hashed_password = hash_password(password)
        cursor.execute('''SELECT * FROM users WHERE email = ? AND password = ?;''',
                       (email, hashed_password))
        user = cursor.fetchone()
        if user:
            st.session_state.authenticated = True
            st.session_state.user_data = {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'password': user[3]
            }
            st.success("✅ Login successful!")
            # st.rerun()
            # ✅ Debug: Print all users
            cursor.execute('SELECT * FROM users')
            return True
        else:
            st.error("❌ Invalid email or password.")
            return False
    except sqlite3.DatabaseError as e:
        st.error(f"❌ Database error occurred: {e}")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")
    return False

st.title("🔐 Secure Data Encryption System")
st.write("Powered by Streamlit + SQLite + SHA-256 + Fernet")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

if not st.session_state.authenticated:
    choice = st.radio("Select an option:", ["Login", "Signup"], horizontal=True)

    if choice == "Signup":
        st.subheader("Create a New Account")
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            if name and email and password:
                signup(name, email, password)
            else:
                st.warning("Please fill out all fields.")

    elif choice == "Login":
        st.subheader("Login to Your Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if email and password:
                login(email, password)
            else:
                st.warning("Please enter both email and password.")
else:
    st.success(f"👋 Welcome, {st.session_state.user_data['name']}!")
    action = st.radio("Choose an action:", ["Insert Data", "Retrieve Data", "Logout"], horizontal=True)

    if action == "Insert Data":
        st.subheader("🔒 Insert New Data")
        plain_data = st.text_area("Enter data to encrypt")
        passkey = st.text_input("Encryption Key", type="password")
        if st.button("Encrypt & Save"):
            if plain_data and passkey:
                insert_data(plain_data, passkey, st.session_state.user_data['id'])
            else:
                st.warning("Please provide both data and encryption key.")

    elif action == "Retrieve Data":
        st.subheader("📂 Retrieve Your Data")
        passkey = st.text_input("Enter your Encryption Key", type="password")
        if st.button("Fetch and Decrypt"):
            data_entries = get_encrypted_data(st.session_state.user_data['id'])
            if not data_entries:
                st.info("No data found.")
            else:
                decryted_data_list = []
                for i, (enc_data,) in enumerate(data_entries, 1):
                    decryptd_d =  decrypt_data(enc_data, passkey)
                    if "Decryption failed!" not in decryptd_d:
                        decryted_data_list.append(decryptd_d)

                if not decryted_data_list:
                    st.error("❌ Decryption failed! No data found with this passkey - Incorrect passkey or corrupted data.")
                else:   
                    st.success("✅ Decrypted data:")
                    for i, v in enumerate(decryted_data_list, 1):
                        st.code(f"{v}")
                    st.markdown("---")

    elif action == "Logout":
        st.subheader("⚠️ Confirm Logout")
        st.warning("Are you sure you want to logout?")
        
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.user_data = {}
            st.success("✅ Logged out successfully.")
            st.rerun()

