class UserProfile:

    def __init__(self, username, password):
        self.username = username
        self.first_name = password

    def login(self):
        if self.username == input(f"Enter your username: "):
            print(f"Hey username! here's your data: {self.username}")

    # def add_new_data(self):
