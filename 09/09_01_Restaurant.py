class Restaurant:
    """A simple attemt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"This restaurant's name is {self.restaurant_name.title()} and its cuisine is type {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        """Indicates that restaurant is open."""
        print(f"The restaurant is OPEN.")


restaurant = Restaurant('casa xto', 'asador')

print(f"The name of my restaurant is {restaurant.restaurant_name.title()}.")
print(f"My restaurant's cuisine type is {restaurant.cuisine_type.title()}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()