import unittest
from my_lambdata.restaurant import Restaurant

class TestRestaurant(unittest.TestCase):


    def test_describe(self):
        restaurant1 = Restaurant("Banana Leaf", "Thai", "111, Long Island")
        restaurant2 = Restaurant("RAJ", "Indian")
        restaurant1.describe_restaurant()
        restaurant2.describe_restaurant()
        self.assertEqual(restaurant1.restaurant_name, "Banana Leaf")
        self.assertEqual(restaurant2.cuisine_type, "Indian")
        self.assertEqual(restaurant2.describe_restaurant(), 'RAJ is selling Indian food.')

    def test_open(self):
        restaurant3 = Restaurant("Leaf", "Thai")
        self.assertEqual(restaurant3.restaurant_open(),'Leaf is open now.')

    def test_closed(self):
        restaurant4 = Restaurant("Ketty", "Thai")
        self.assertEqual(restaurant4.restaurant_closed(),'Ketty is closed now.')
    

if  __name__ == "__main__":
    unittest.main()
