import unittest
from unittest.mock import patch
from auth import Auth
from database import save_users, load_users


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.auth = Auth()

        # reset users for testing
        save_users([
            {"username": "admin", "password": "1234"}
        ])

    # ---------------- LOGIN TESTS ----------------

    @patch("builtins.input", side_effect=["admin", "1234"])
    def test_login_success(self, mock_input):
        result = self.auth.login()
        self.assertEqual(result, "admin")

    @patch("builtins.input", side_effect=["admin", "asad", "admin", "1234"])
    def test_login_retry_then_success(self, mock_input):
        result = self.auth.login()
        self.assertEqual(result, "admin")

    # ---------------- SIGNUP TESTS ----------------

    @patch("builtins.input", side_effect=["newuser", "pass123"])
    def test_signup_success(self, mock_input):
        result = self.auth.signup()
        self.assertEqual(result, "newuser")

    @patch("builtins.input", side_effect=["admin", "1234"])
    def test_signup_existing_user(self, mock_input):
        result = self.auth.signup()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()