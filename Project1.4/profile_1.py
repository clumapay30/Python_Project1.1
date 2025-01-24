import json
import os

class Profile:
    def __init__(
        self, username, password, first_name="", last_name="", email="", phone=int):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.new_data = {
            self.username: {
                "password": self.password,
                "First Name": self.first_name,
                "Last Name": self.last_name,
                "Email": self.email,
                "Phone": self.phone,
            }
        }

    def create_user(self):
        if not os.path.exists("data.json"):
            with open("data.json", "w") as data_file:
                json.dump(self.new_data, data_file, indent=4)
        else:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(self.new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def read_data(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            if self.username not in data:
                print(f"Wrong Credentials! Please try again.")

            else:
                # with open("data.json", "r") as data_file:
                #     data = json.load(data_file)
                print(f"Welcome {self.username}! You have logged in.")
                print(data[self.username])

    def update_user(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            if self.username not in data:
                print(f"Missing data")
            else:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(self.new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

    def delete_user(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            del data[self.username]
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
