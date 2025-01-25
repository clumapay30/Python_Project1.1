from config import *


class Controllers(Config):

    def __init__(self):
        super().__init__()
        # print(f"\n")
        print(f"Initializing Project Emeperor!")
        print(f"How can I help? \n")
        self.register_user()

    def login_control(self):
        control = input(f"Login or Register? ").lower()
        if control == "login":
            self.login_user()
        elif control == "register":
            self.register_user()
            
    def update_or_delete_control(self):
        update_status = input(f"Type 'Delete' or 'Update': ").lower()
        if update_status  == 'delete':
            verify_username = input(f"Verify your username: ")
            verify_password = input(f"Verify your password: ")
            self.delete_user(verify_username, verify_password)
        elif update_status == 'update':
            self.update_user()
    
    def register_user(self):
        username = input(f"Enter a username: ")
        password = input(f"Enter a password: ")
        firstname = input(f"Enter your first name: ")
        lastname = input(f"Enter your last name: ")
        email = input(f"Enter valid email: ")

        self.data_control(
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            type="register",
        )
        

    def login_user(self):
        username = input("Username: ")
        password = input("Password: ")

        success = (self.read(username=username, password=password))
            
        if success == False:
            self.login_control()
        elif success == True:
            self.update_or_delete_control()
            
    def update_user(self):
        username = input(f"Enter a username: ")
        password = input(f"Enter a password: ")
        firstname = input(f"Enter your first name: ")
        lastname = input(f"Enter your last name: ")
        email = input(f"Enter valid email: ")

        self.data_control(
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            type="update",
        )

    def delete_user(self, username, password):
        validator = self.delete(username, password)
        if validator == False:
            self.update_or_delete_control()
        else:
            self.login_control()
        
    def logout_user(self):
        print(f"You have been logged out!")
        self.login_control()
