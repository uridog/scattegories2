import hashlib
import threading
import sqlite3

connection = sqlite3.connect("users.db")


def build_db():
    print("111", threading.get_native_id())
    connection.execute("""CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL, firstname TEXT NOT NULL, 
    lastname TEXT NOT NULL, password TEXT NOT NULL) """)


def check_password(username,password):
    # Check if the username already existsbn  bn
    query = 'SELECT password FROM users WHERE username = ?'
    connection.execute(query, (username,))
    result = connection.fetchone()
    if password == result:
        return True
    return False


def check_if_in_db(username):
    # Check if the username already exists
    print("XDF")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print("fg")
    connection.execute(query)
    print("fth")
    result = connection.fetchall()
    print(result[0])
    if result:
        # Username already exists
        return False
    return True

def select_user_by_id(self, username):
        print("Opened database successfully")
        str1 = "select*from users"
        strsql = "SELECT userId, username, password, email  from " + \
                 self.tablename + " where " + self.userId + "=" + str(username)
        print(str1)
        cursor = connection.execute(str1)


def add_user_sql(username, firstname, lastname, password):
    # Check if the username already exists
    query = 'SELECT * FROM users WHERE username = ?'
    connection.execute(query, (username,))
    result = connection.fetchone()
    if result:
        # Username already exists
        return False

        # Encrypt the password using md5 hash function
    password = hashlib.md5(password.encode('latin-1')).hexdigest()

    # Insert the new user into the users table values = (username, firstname, lastname,
    # password) query = "INSERT INTO users (username, firstname, lastname, password) VALUES (
    # ?, ?, ?, ?)" cur.execute(query, values)
    connection.execute(
        "INSERT INTO users (username, firstname, lastname,password) VALUES (?, ?, ?, ?)",
        (username, firstname, lastname, password))

    # Commit the transaction
    connection.commit()

    return True
