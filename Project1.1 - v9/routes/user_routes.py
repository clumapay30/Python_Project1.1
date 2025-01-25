from database.db import *


class User_Routes:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def check_users_table(self):
        conn = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                           CREATE TABLE IF NOT EXISTS users (
                               id SERIAL PRIMARY KEY,
                               firstname VARCHAR(100) NOT NULL,
                               lastname VARCHAR(100) NOT NULL,
                               email VARCHAR(100) UNIQUE NOT NULL,
                               username VARCHAR(100) UNIQUE NOT NULL,
                               password VARCHAR(100)
                           )
                           """
            )

            self.conn.commit()
            print("Table 'users' is ready!")
        except Exception as e:
            print(f"Error ensuring table: {e}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                cursor.close()
                self.db.release_connection(conn)

    def create_user(self, firstname, lastname, email, username, password):
        self.check_users_table()
        try:
            cursor = self.conn.cursor()

            insert_query = "INSERT INTO users(firstname, lastname, email, username, password) VALUES (%s, %s, %s, %s, %s);"
            user_data = (firstname, lastname, email, username, password)

            cursor.execute(insert_query, user_data)

            self.conn.commit()
            print("Data inserted successfully!")

        except psycopg2.Error as e:
            print(f"An error occurred: {e}")

        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()

    def read_user(self, username, password):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            user_data = (username, password)

            cursor.execute(query, user_data)

            data = cursor.fetchone()

            # self.conn.commit()
            
            print("You have logged in!")
            print(f"Data: {data[0]}")

        except psycopg2.Error as e:
            print(f"An error occurred: {e}")

        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()

    def update_user(self, firstname, lastname, username):
        try:
            cursor = self.conn.cursor()

            query = """
            UPDATE users 
            SET firstname = %s, lastname = %s 
            WHERE username = %s;
            """
            params = (firstname, lastname, username)

            cursor.execute(query, params)

            self.conn.commit()

        except psycopg2.Error as e:
            print(f"An error occurred: {e}")

        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()

    def delete_user(self, username, password):
        try:
            cursor = self.conn.cursor()

            delete_query = "DELETE FROM users WHERE username = %s AND password = %s"
            user_data = (username, password)
            
            cursor.execute(delete_query, user_data)
            self.conn.commit()
            print(f"User {username} deleted successfully!")

        except psycopg2.Error as e:
            print(f"An error occurred: {e}")
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()

    def delete_table(self):
        try:
            cursor = self.conn.cursor()
            drop_table_query = "DROP TABLE IF EXISTS users;"

            cursor.execute(drop_table_query)
            self.conn.commit()
            print(f"Table 'Users' deleted successfully!")

        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()
