import json


class Profile:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.new_data = {
            self.username: {
                "email": self.email, 
                "password": self.password
                }
        }

    def check_data(self):
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if data[self.username]['password'] == self.password:
                print(f'Congratulations! You have logged in')
            else:
                print(f'Oops! Wrong credentials!')

    def add_or_update_data(self):
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(self.new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    # def add_new_user(self):
    #     with open("data.json", "w") as data_file:
    #         json.dump(self.new_data, data_file, indent=4)
