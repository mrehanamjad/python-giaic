# 🔐 Secure Data Encryption System (SDES)

A secure, user-friendly web application built with **Streamlit** that enables users to **encrypt, store, and retrieve sensitive data** using **SHA-256 hashing** and **Fernet symmetric encryption**. This version stores all data locally in a **JSON file**, making it lightweight and easy to deploy without a database.

---

## Live Site: [Secure Data Encryption System](https://sdes-secure-data-encryption-system.streamlit.app/)



## 🚀 Features

* 🧑‍💻 User Signup & Login (passwords hashed using SHA-256)
* 🔐 Data Encryption using `cryptography.Fernet`
* 🔓 Data Decryption (with correct key)
* 🗃️ Securely stores encrypted data per user in a local JSON file
* ✅ Simple and intuitive interface using Streamlit
* 🔐 Safe logout functionality

---

## 🛠️ Technologies Used

* [Streamlit](https://streamlit.io/) – UI and application framework
* [cryptography](https://cryptography.io/) – Secure encryption (Fernet)
* [hashlib](https://docs.python.org/3/library/hashlib.html) – Password hashing (SHA-256)
* [uuid](https://docs.python.org/3/library/uuid.html) – Unique user ID generation
* `JSON` – Used as a local file-based data store

---

## ✅ How to Run the Project

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/sdes.git
cd sdes
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Application**

```bash
streamlit run sdes_app.py
```

---

## 📌 Usage

* **Sign Up**: Create an account with name, email, and password.
* **Login**: Authenticate with email and password.
* **Insert Data**: Enter plain text and an encryption key to securely store data.
* **Retrieve Data**: Enter the same encryption key to view your previously stored data.
* **Logout**: Ends the session securely.

> 🔑 Make sure to **remember your encryption key**, as it is required to decrypt your stored data.

---

## 🧪 Example

1. Register as a new user.
2. Insert secret notes like:

   * "My bank pin is 1234"
   * "Secret project password: xyz123"
3. Retrieve them only with the same passkey you used to encrypt.

---

## 🔒 Security Notes

* Passwords are hashed before storing.
* Each user’s data is encrypted separately using their own passkey.
* Data and users are saved in local JSON files (`users.json`, `data.json`).
* No sensitive data is stored in plaintext.

---

## 🧠 Future Improvements

* Add password reset functionality
* Multi-layered encryption
* Integration with cloud databases (MongoDB, SQLite, etc.)
* User activity logs and session tracking
