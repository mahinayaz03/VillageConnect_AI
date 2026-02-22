import unittest
from chatbot import get_response

class TestVillageConnect(unittest.TestCase):

    def test_valid_query(self):
        response, score = get_response("government scheme")
        self.assertIsInstance(response, str)
        self.assertGreaterEqual(score, 0)

    def test_invalid_query(self):
        response, score = get_response("asdfghjklqwerty")
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()