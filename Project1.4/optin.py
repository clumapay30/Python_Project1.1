from profile_1 import *


class OptinForm(Profile):

    def __init__(self):
        self.user_form()

    def user_form(self):
        self.user_input = input(f"Type 'Register' or 'Login': ").lower()
        
        login = True
        while login:
            if self.user_input == "register":
                self.register_user()
                login = False
            elif self.user_input == "login":
                self.login_user()
                login = False
            else:
                print(
                    f"Oops! You can only type 'Register' or 'Login' to proceed! Please try again: "
                )
                self.user_form()

    def register_user(self):
        self.first_name = input(f"Enter your First Name: ")
        self.last_name = input(f"Enter your Last Name: ")
        self.email = input(f"Enter your Email: ")
        self.phone = int(input(f"Enter your Phone: "))
        self.username = input(f"Enter Username: ")
        self.password = input(f"Enter Password: ")

        new_user = Profile(
            self.username,
            self.password,
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
        )
        new_user.create_user()

    def update_user(self):
        self.first_name = input(f"Enter your First Name: ")
        self.last_name = input(f"Enter your Last Name: ")
        self.email = input(f"Enter your Email: ")
        self.phone = int(input(f"Enter your Phone: "))
        self.username = input(f"Enter Username: ")
        self.password = input(f"Enter Password: ")

        new_user = Profile(
            self.username,
            self.password,
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
        )
        new_user.update_user()

    def login_user(self):
        self.username = input(f"Enter Username: ")
        self.password = input(f"Enter Password: ")

        login_user = Profile(self.username, self.password)
        login_user.read_data()

    def logout_user(self):
        # self.user_form()
        pass
