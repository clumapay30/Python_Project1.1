# crud.py
from db import get_connection, release_connection

def create_user(name, email):
    """
    Insert a new user into the database, ensuring the table exists first.
    """
    ensure_users_table()  # Ensure the table exists

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Insert data
        cursor.execute("""
            INSERT INTO users (name, email)
            VALUES (%s, %s)
        """, (name, email))

        conn.commit()
        print("User created successfully!")

    except Exception as e:
        print(f"Error creating user: {e}")
        if conn:
            conn.rollback()

    finally:
        if conn:
            cursor.close()
            release_connection(conn)

def get_users():
    """
    Fetch all users from the database.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Query data
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return users

    except Exception as e:
        print(f"Error fetching users: {e}")
        return []

    finally:
        if conn:
            cursor.close()
            release_connection(conn)


def ensure_users_table():
    """
    Ensure the 'users' table exists in the database.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """)

        conn.commit()
        print("Table 'users' is ready!")

    except Exception as e:
        print(f"Error ensuring table: {e}")
        if conn:
            conn.rollback()

    finally:
        if conn:
            cursor.close()
            release_connection(conn)