from control import create_user, get_users

name = input(f"Enter your name: ")
email = input(f"Enter you email: ")

create_user(name, email)

users = get_users()
for user in users:
    print(user)
