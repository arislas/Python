class Restaurant:
    """A simple attemt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant's name and cuisine type."""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"This restaurant's name is {self.restaurant_name.title()} and its cuisine is type {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        """Indicates if the restaurant is open."""
        print(f"The restaurant is OPEN.")

restaurant1 = Restaurant('casa xto', 'asador')
restaurant2 = Restaurant('la visión', 'chino')
restaurant3 = Restaurant('el pozo', 'pizzeria')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()