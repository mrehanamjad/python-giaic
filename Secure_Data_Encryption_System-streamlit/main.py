import hashlib
import streamlit as st
from cryptography.fernet import Fernet
import base64
import uuid
import json
import os

# JSON file paths
USERS_FILE = "users.json"
DATA_FILE = "data.json"

# Ensure files exist
for file in [USERS_FILE, DATA_FILE]:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)

# Helper functions for JSON storage
def load_json(file):
    with open(file, 'r') as f:
        return json.load(f)

def save_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# Password hashing
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Encryption key generator
def generate_key(passkey: str) -> bytes:
    hashed_passkey = hashlib.sha256(passkey.encode()).digest()
    return base64.urlsafe_b64encode(hashed_passkey)

# Encryption and decryption
def encrypt_data(data: str, passkey: str) -> str:
    key = generate_key(passkey)
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str, passkey: str) -> str:
    key = generate_key(passkey)
    fernet = Fernet(key)
    try:
        return fernet.decrypt(encrypted_data.encode()).decode()
    except Exception:
        return "Decryption failed! Incorrect passkey or corrupted data."

# Signup function
def signup(name: str, email: str, password: str):
    users = load_json(USERS_FILE)
    if any(u['email'] == email for u in users):
        st.error("Email already exists.")
        return
    _id = str(uuid.uuid4())
    hashed = hash_password(password)
    user = {"id": _id, "name": name, "email": email, "password": hashed}
    users.append(user)
    save_json(USERS_FILE, users)
    st.success("User registered successfully!")
    st.session_state.authenticated = True
    st.session_state.user_data = user
    st.rerun()

# Login function
def login(email: str, password: str) -> bool:
    users = load_json(USERS_FILE)
    hashed = hash_password(password)
    user = next((u for u in users if u['email'] == email and u['password'] == hashed), None)
    if user:
        st.session_state.authenticated = True
        st.session_state.user_data = user
        st.success("Login successful!")
        st.rerun()
        return True
    else:
        st.error("Invalid email or password.")
        return False

# Insert data
def insert_data(data: str, passkey: str, user_id: str):
    encrypted = encrypt_data(data, passkey)
    db = load_json(DATA_FILE)
    db.append({"encrypted_data": encrypted, "user_id": user_id})
    save_json(DATA_FILE, db)
    st.success("Data inserted successfully!")

# Fetch and decrypt data
def get_encrypted_data(user_id: str) -> list:
    db = load_json(DATA_FILE)
    return [entry["encrypted_data"] for entry in db if entry["user_id"] == user_id]

# Streamlit UI
st.title("🔐 Secure Data Encryption System")
st.write("Now using Streamlit + JSON + SHA-256 + Fernet")

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
                decrypted_list = [decrypt_data(enc, passkey) for enc in data_entries]
                valid_data = [d for d in decrypted_list if "Decryption failed!" not in d]
                if not valid_data:
                    st.error("Decryption failed! Incorrect passkey or corrupted data.")
                else:
                    st.success("Decrypted data:")
                    for d in valid_data:
                        st.code(d)

    elif action == "Logout":
        st.subheader("⚠️ Confirm Logout")
        st.warning("Are you sure you want to logout?")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.user_data = {}
            st.success("Logged out successfully.")
            st.rerun()
