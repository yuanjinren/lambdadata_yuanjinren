class Restaurant:
    restaurant_address = 'unknown'

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        description = (self.restaurant_name + ' is selling ' 
                    + self.cuisine_type + ' food.')
        return description.format()

    def restaurant_open(self):
        print(self.restaurant_name.title() + " is open now. ")

    def restaurant_closed(self):
        print(self.restaurant_name.title() + " is closed now. ")

if __name__ == "__main__":

    restaurant1 = Restaurant("Banana Leaf", "Thai")
    restaurant1.restaurant_address = "111, Long Island"
    print(restaurant1.describe_restaurant() + " and its address is " + restaurant1.restaurant_address + '.')
    restaurant1.restaurant_open()

    restaurant2 = Restaurant("RAJ", "Indian")
    print(restaurant2.describe_restaurant() + " and its address is " + restaurant2.restaurant_address + '.')
    restaurant2.restaurant_closed()
