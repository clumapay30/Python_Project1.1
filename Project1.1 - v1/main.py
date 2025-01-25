from Profile import *


def sign_in():
    login = True
    
    while login:
        username = input(f"Enter username: ")
        password = input(f"Enter password: ")

        profile = Profile(username, password)
        
        check_profile = profile.check_credentials()
        
        if check_profile == False:
            sign_in()
        

        login = False


sign_in()
