from user_profile import *


login_option = True
while login_option:
    user_input = input(f"Please type 'Register' or 'Login' to proceed: ").lower()

    if user_input == "register":
        email = input(f"Enter valid email: ")
        username = input(f"Enter username: ")
        password = input(f"Enter password: ")
        
        register_user = Profile(username, email, password)
        register_user.add_or_update_data()

        login_option = False
    elif user_input == "login":
        email= input(f"Enter valid email: ")
        username = input(f"Enter username: ")
        password = input(f"Enter password: ")

        login_user = Profile(username, email, password)
        login_user.check_data()
        
        
        login_option = False
    else:
        print(f"Oops! You're typing '{user_input}' which is not the option!")

