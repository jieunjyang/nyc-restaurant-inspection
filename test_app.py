import unittest
import sys,os
import app as app
from models import db, Restaurants


class AppTestcase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        assert b'Hello World.' in response.data

    def test_get_all_restaurants(self):
        restaurant = Restaurants(123, 'name_of_rest', 'boro1', 'building1', 'street1', '12345', '1234567890', 'Thai')
        response = self.app.get("/api/v1/restaurants")
        self.assertEqual(response.status_code, 201)

    def test_get_restaurants_by_category(self):
        response = self.app.get("/api/v1/restaurants/Thai")
        self.assertEqual(response.status_code, 201)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AppTestcase('test_index_route'))
    suite.addTest(AppTestcase('test_get_all_restaurants'))
    suite.addTest(AppTestcase('test_get_restaurants_by_category'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
