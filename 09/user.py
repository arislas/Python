class User:
    """A simple attemp to model an user."""

    def __init__(self, first_name, last_name, email, password):
        """Initialize first and last name of an user."""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = 0
    
    def describe_user(self):
        """Describe an user."""
        
        print("User's summary:")
        print(f"- Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"- e-mail: {self.email}")
        print(f"- Password: {self.password}")
    
    def greet_user(self):
        """Greet an user."""

        print(f"Hello, {self.first_name.title()}!")
    
    def increment_login_attempts(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0