import unittest
import orders

class PhoneValidationTest(unittest.TestCase):
    def test_valid_phone(self):
        # Положительный тест: валидный номер телефона
        phone = "+71234567890"
        result = orders.validate_phone(phone)
        self.assertTrue(result)

    def test_valid_phone_with_spaces(self):
        # Положительный тест: валидный номер телефона с пробелами
        phone = "+7 123 456 78 90"
        result = orders.validate_phone(phone)
        self.assertTrue(result)

    def test_valid_phone_with_dash(self):
        # Положительный тест: валидный номер телефона с дефисами
        phone = "+7-123-456-78-90"
        result = orders.validate_phone(phone)
        self.assertTrue(result)

    def test_valid_phone_with_parentheses(self):
        # Положительный тест: валидный номер телефона с круглыми скобками
        phone = "+7 (123) 456-78-90"
        result = orders.validate_phone(phone)
        self.assertTrue(result)

    def test_valid_phone_with_multiple_plus_signs(self):
        # Положительный тест: валидный номер телефона с несколькими плюсами
        phone = "++7 (123) 456-78-90"
        result = orders.validate_phone(phone)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()