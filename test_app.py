import sys,os
import unittest

import app as app


class AppTestcase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.assertIsNotNone(app)

    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World.', response.data)

    def test_get_all_restaurants(self):
        response = self.app.get("/api/v1/restaurants")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_get_restaurants_by_category(self):
        response = self.app.get("/api/v1/restaurants/Thai")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AppTestcase('test_index_route'))
    suite.addTest(AppTestcase('test_get_all_restaurants'))
    suite.addTest(AppTestcase('test_get_restaurants_by_category'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
