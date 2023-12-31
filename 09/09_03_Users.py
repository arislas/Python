class User:
    """A simple attemp to model an user."""

    def __init__(self, first_name, last_name, email, password):
        """Initialize first and last name of an user."""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def describe_user(self):
        """Describe an user."""
        
        print("User's summary:")
        print(f"- Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"- e-mail: {self.email}")
        print(f"- Password: {self.password}")
    
    def greet_user(self):
        """Greet an user."""

        print(f"Hello, {self.first_name.title()}!")


user1 = User('xto', 'sarcior', 'arislas@gmail.com', 'contraseña')
user2 = User('yoston', 'sarcior', 'yoston@gmail.com', 'password')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()