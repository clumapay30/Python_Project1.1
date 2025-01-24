import json
import os

class Config:
    
    def __init__(self):
        self.data = {}
        # print("Data initializing!")

    def data_control(self, **kwargs) -> None:
        new_data = {
            kwargs["username"]: {
                "firstname": kwargs["firstname"],
                "lastname": kwargs["lastname"],
                "email": kwargs["email"],
                "username": kwargs["username"],
                "password": kwargs["password"],
            }
        }
        
        if kwargs["type"] == "register":
            self.data = new_data
            self.create()
            print(f"Welcome aboard {kwargs["firstname"]}")
        elif kwargs["type"] == "update":
            self.data = new_data
            self.update(kwargs["username"])
            print(f"Your data has been updated {kwargs["firstname"]}")

    def create(self):
        if not os.path.exists("data.json"):
            with open("data.json", "w") as file:
                json.dump(self.data, file, indent=4)
        else:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(self.data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
    
    def read(self, username: str, password: str):
        with open("data.json", "r") as file:
            data = json.load(file)
            if username not in data or password != data[username]["password"]:
                print(f"Oops! Wrong Credentials. Please try again! \n")
                return False
            else:
                print(f"Welcome back {data[username]["firstname"]}! \n")
                return True
        
    def update(self, username):
        with open("data.json", "r")as file:
            data = json.load(file)
            data.update(self.data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def delete(self, username: str, password: str):
        with open("data.json", "r") as file:
            data = json.load(file)
            if username not in data or password != data[username]["password"]:
                print(f"Oops! Wrong credentials")
                return False
            else:
                print("data found")
                del data[username]
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        print(f"The user {username} has been deleted! \n")