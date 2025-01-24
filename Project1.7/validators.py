import json
import os


class Validators:

    def __init__(self, username, password):
        self.username: str = username
        self.password: str = password

    def validate(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        if self.username not in data:
            # print("Wrong credentials!")
            print(f"New user!")
            return False
        else:
            # Check this validator later
            # print(f"Welcome back {data[self.username]["firstname"]}")
            return True
