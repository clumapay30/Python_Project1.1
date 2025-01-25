class Register:
    
    def __init__(self, new_username, new_password):
        self.username = new_username
        self.password = new_password
        
    
    def register_user(self):
        username = input(f"Register username: ")
        password = input(f"Register password: ")
        
        return {
            username: {
                'password': password
            }
        }
        
        
    