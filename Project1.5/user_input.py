from application import *


class UserInputs:

    def __init__(self):
        self.app = Application()
        self.login_status()

    def login_status(self):
        user = True
        while user:
            user_type = input(f"Type 'Login' or 'Register': ").lower()
            if user_type == "register":
                self.register()
                user = False
            elif user_type == "login":
                self.login()
                user = False
            else:
                print(f"Oops '{user_type}' is not the option")
                self.login_status()

    def navigation(self, username):
        status = True
        while status:
            update_user = input(f"Hey {username}, do you want to 'Delete', 'Update' or 'Logout'?: ").lower()
            if update_user == "update":
                self.update_user(username)
                status = False
            elif update_user == "delete":
                self.delete_user(username)
                status = False
            elif update_user == "logout":
                self.logout(username)
                status = False
            else:
                print(f"Oops! you're typing beyond imagination.")
                self.navigation(username)

    def login(self):
        username = input(f"Enter username: ")
        password = input(f"Enter password: ")

        status = self.app.read(username=username, password=password)
        if status == False:
            self.login_status()

        self.navigation(username)

    def register(self):
        first_name = input(f"Please enter your First name: ")
        last_name = input(f"Please enter your Last name: ")
        username = input(f"Please enter username: ")
        password = input(f"Please enter password: ")
        email = input(f"Please enter valid email: ")
        phone = int(input(f"Please enter Phone number: "))

        self.app.data_shell(
            firstname=first_name,
            lastname=last_name,
            username=username,
            password=password,
            email=email,
            phone=phone,
            type="register",
        )

        self.update_user(username)
        self.navigation(username)

    def update_user(self, username):
        update_user = input(f"Do you want to update? Y/N: ").lower()
        if update_user == "y" or update_user == "yes":
            first_name = input(f"Please enter your First name: ")
            last_name = input(f"Please enter your Last name: ")
            password = input(f"Please enter password: ")
            email = input(f"Please enter valid email: ")
            phone = int(input(f"Please enter Phone number: "))
            
            self.app.data_shell(
            type=update_user,
            firstname=first_name,
            lastname=last_name,
            password=password,
            email=email,
            phone=phone,
            username=username,
        )
        else:
            print(f'Thank you for your time {username}!')

        self.navigation(username)

    def delete_user(self, username):
        self.app.delete(username)
        self.login_status()

    def logout(self, username):
        print(f"Hey {username}, you have been logout! Thank you for your time")
        self.login_status()
