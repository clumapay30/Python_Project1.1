from Register import *

class Profile(Register):
    users = {
            'username1': {"password": 'password1'},
            'username2': {"password": 'password2'},
        }
    
    def __init__(self, username, password):
        super().__init__(
            new_username=username,
            new_password=password
        )
        self.username = username
        self.password = password

    def check_credentials(self):
        if self.username not in self.users:
            print(f'Oops! wrong credentials')
            self.not_user()
            return False
        elif self.password == self.users[self.username]["password"]:
            print(f"Congratulation {self.username}, you logged in successfully!")
        else:
            print(f"Wrong credentials! Please try again")
            return False

    def not_user(self):
        register = input(f"Do you want to register? (Y/N): ")

        if register == 'Y' or register == 'yes':
            new_user = self.register_user()
            self.users.update(new_user)
            print(self.users)
            self.check_credentials()

