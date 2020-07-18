class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type, restaurant_address = 'unknown'):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_address = restaurant_address

    def describe_restaurant(self):
        return '{} is selling {} food.'.format(self.restaurant_name,self.cuisine_type)

    def restaurant_open(self):
        return '{} is open now.'.format(self.restaurant_name)

    def restaurant_closed(self):
        return '{} is closed now.'.format(self.restaurant_name)

if __name__ == "__main__":

    restaurant1 = Restaurant("Banana Leaf", "Thai", "111, Long Island")
    print(restaurant1.describe_restaurant())
    print(restaurant1.restaurant_open())

    restaurant2 = Restaurant("RAJ", "Indian")
    print(restaurant2.describe_restaurant())
    print(restaurant2.restaurant_closed())
