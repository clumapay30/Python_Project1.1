# JSON Data Option
# Write using json.dump()
# Read using json.load()
# Update json.update()

import json

username = input(f"Enter username: ")
email = input(f"Enter your email address: ")
password = input(f"Enter a password: ")
print(password)

new_data = {
    username: {
        "email": email,
        "password": password
    }
}

# Write data
# with open("./file_managing/data.json", "w") as data:
#     json.dump(new_data, data, indent=2)

# Read data
# with open("./file_managing/data.json", "r") as data_file:
#     data = json.load(data_file)
#     print(data[username]['password'])

# Update data
with open("./file_managing/data.json", "r") as data_file:
    data = json.load(data_file)
    data.update(new_data)
    print(data)
    
with open("./file_managing/data.json", "w") as data_file:
    json.dump(data, data_file, indent=4)
    
