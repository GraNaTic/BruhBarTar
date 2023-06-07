import unittest
import orders

class PhoneValidationTest(unittest.TestCase):
    def test_valid_phone(self):
        phone = "+71234567890"
        result = orders.validate_phone(phone)
        self.assertTrue(result)

    def test_phone_with_spaces(self):
        phone = "+7 123 456 78 90"
        result = orders.validate_phone(phone)
        self.assertFalse(result)

    def test_phone_with_dash(self):
        phone = "+7-123-456-78-90"
        result = orders.validate_phone(phone)
        self.assertFalse(result)

    def test_phone_with_parentheses(self):
        phone = "+7 (123) 456-78-90"
        result = orders.validate_phone(phone)
        self.assertFalse(result)

    def test_phone_with_multiple_plus_signs(self):
        phone = "++7 (123) 456-78-90"
        result = orders.validate_phone(phone)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()