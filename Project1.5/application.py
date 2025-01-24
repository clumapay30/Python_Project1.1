import json
import os


class Application:

    def __init__(self):
        self.data: dict = {}
        print(self.data)

    def data_shell(self, **kwargs) -> dict:
        new_data = {
            kwargs["username"]: {
                "firstName": kwargs["firstname"],
                "lastName": kwargs["lastname"],
                "email": kwargs["email"],
                "phone": kwargs["phone"],
                "username": kwargs["username"],
                "password": kwargs["password"],
            }
        }

        if kwargs["type"] == "register":
            self.data = new_data
            self.create(kwargs["firstname"])
        elif kwargs["type"] == "y" or kwargs["type"] == "yes":
            self.data = new_data
            self.update(kwargs["username"])

        print(self.data)

    def create(self, firstname: str) -> None:
        if not os.path.exists("data.json"):
            print(f"File not exists! I'm creating a file for you.")
            with open("data.json", "w") as file:
                json.dump(self.data, file, indent=4)
        else:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(self.data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        print(f"Welcome aboard {firstname}")

    def read(self, username: str, password: str) -> bool:
        with open("data.json", "r") as file:
            data = json.load(file)
            if username not in data or password != data[username]["password"]:
                print(f"Oops Wrong credentials! Please try again.")
                return False
            else:
                print(f"Welcome back {data[username]['firstName']}! you have login")
                print(data[username])
                return True

    def update(self, username: str):
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(self.data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        
        print(f"Hey {username}, your profile has been update: \n{self.data}")

    def delete(self, username):
        with open("data.json", "r") as file:
            data = json.load(file)
            del data[username]
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"The user {username} has been deleted!")
