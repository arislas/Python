from user import User

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
        self.privileges = Privileges()