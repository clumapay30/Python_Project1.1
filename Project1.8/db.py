import psycopg2
from psycopg2 import pool

# Connection parameters
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Simplepersonitsme",
    "host": "localhost",  # Or your server address
    "port": 5432          # Default PostgreSQL port
}

try:
    # Establish the connection
    conn = psycopg2.connect(**DB_CONFIG)
    print("Connection successful!")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example: Fetching PostgreSQL version
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"PostgreSQL version: {version[0]}")

    # Close the cursor and connection
    cursor.close()
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")


# Create a connection pool
connection_pool = pool.SimpleConnectionPool(1, 10, **DB_CONFIG)

def get_connection():
    """
    Get a connection from the connection pool.
    """
    try:
        return connection_pool.getconn()
    except Exception as e:
        print(f"Error getting connection: {e}")
        raise

def release_connection(conn):
    """
    Return a connection to the pool.
    """
    try:
        connection_pool.putconn(conn)
    except Exception as e:
        print(f"Error releasing connection: {e}")
        raise

def close_all_connections():
    """
    Close all connections in the pool.
    """
    connection_pool.closeall()