# Create a class with private attributes and access them using methods.

class USERS:
    def __init__(self, name, email):
        self.name = name 
        self.email = email

class view_account(USERS):
    def __init__(self, name, email, password):
        super().__init__(name, email)
        self.__password = password

    @property
    def get_access(self):
        return self.__password

user1 = view_account("Gayathri", "gaya@gmail.com", "G9094")

print(user1.name)
print(user1.email)
print(user1.get_access)



        


