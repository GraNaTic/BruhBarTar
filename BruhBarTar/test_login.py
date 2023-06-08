import unittest
import Grisha

class LoginValidationTest(unittest.TestCase):
    def test_valid_login(self):
        login = "MamaMia"
        result = Grisha.checkLogin(login)
        self.assertTrue(result)

    def test_invalid_login_numbers_only(self):
        login = "123456"
        result = Grisha.checkLogin(login)
        self.assertFalse(result)

    def test_valid_login_with_numbers(self):
        login = "MamaMia2"
        result = Grisha.checkLogin(login)
        self.assertTrue(result)

    def test_invalid_short_login(self):
        login = "Mam"
        result = Grisha.checkLogin(login)
        self.assertFalse(result)

    def test_invalid_long_login(self):
        login = "qwertyuiopweqeeq"
        result = Grisha.checkLogin(login)
        self.assertFalse(result)
