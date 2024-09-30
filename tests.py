import unittest
from app import app


class FlaskTestCase(unittest.TestCase):
    # Test the home route
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Welcome to my simple API!"})

    # Test the add_numbers route with valid numbers
    def test_add_numbers(self):
        tester = app.test_client(self)
        response = tester.get("/add?a=3&b=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 8})

    # Test the add_numbers route with invalid input
    def test_add_invalid_input(self):
        tester = app.test_client(self)
        response = tester.get("/add?a=abc&b=5")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json, {"error": "Invalid input, please provide integers"}
        )


if __name__ == "__main__":
    unittest.main()
