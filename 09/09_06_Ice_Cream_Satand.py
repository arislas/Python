class Restaurant:
    """A simple attemt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"This restaurant's name is {self.restaurant_name.title()} and its cuisine is type {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        """Indicates that restaurant is open."""
        print(f"The restaurant is OPEN.")
    
    def set_number_served(self, number):
        """Set a new number of customers served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increments the number of customers served in the given amount."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """A simple attemt to model an Ice Cream Stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['lemond', 'chocolatte', 'strawberry']
    
    def display_flavors(self):
        print("\nThe list of flavors are:\n")
        for flavor in self.flavors:
            print(f"- {flavor.title()}.")
        print("\n")

ice_cream = IceCreamStand('la guinda', 'ice cream')
ice_cream.display_flavors()