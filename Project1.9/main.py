from routes.user_routes import *

user = User_Routes()

# initialize = input("Type 'Login' or 'Sign Up': ").lower()

# if initialize == 'signup' or initialize == 'sign up':
#     firstname = input("Enter firstname: ")
#     lastname = input("Enter lastname: ")
#     email = input("Enter email: ")
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     user.create_user(firstname, lastname, email, username, password)
# elif initialize == 'login':
#     username = input("Enter username: ")
#     password = input("Enter password: ")
    
#     user.read_user(username, password)  
    
update_data = input("Type 'Delete' or 'Update': ").lower()
if update_data == 'update':
    firstname = input("Enter firstname: ")
    lastname = input("Enter lastname: ")
    username = input("Enter username: ")
            
    user.update_user(firstname, lastname, username)
elif update_data == 'delete':
    username = input("Enter username: ")
    password = input("Enter password: ")

    user.delete_user(username, password)

# initialize = input(f"Type 'Delete' or 'Create' table: ").lower()
# if initialize == "delete":
#     user.delete_table()
# if initialize == "create":
#     user.check_users_table()



    