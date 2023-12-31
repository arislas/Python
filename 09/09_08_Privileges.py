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


class Privileges:
    """Simple attemp to model user's privileges."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print("\nThe privileges of an Andim are:\n")
        for privilege in self.privileges:
            print(f"- {privilege}")
        print("\n")


class Admin(User):
    """A simple attemp to model an admin."""

    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()
    
    #def show_privileges(self):
        #print("\nAdmin's privileges are:\n")
        #for privilege in self.privileges:
            #print(f"- {privilege}")
        #print("\n")


admin = Admin('xto', 'sarcior', 'arislas@gmail.com', 'passwd')
admin.privileges.show_privileges()