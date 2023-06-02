import unittest
import companies

class TestCompanyDescriptionValidation(unittest.TestCase):

    def test_valid_description(self):
        description = "Описание компании. Очень интересное и подробное описание."
        self.assertTrue(companies.validate_description(description))

    def test_empty_description(self):
        description = ""
        self.assertFalse(companies.validate_description(description))

    def test_short_description(self):
        description = "Краткое описание"
        self.assertFalse(companies.validate_description(description))

    def test_long_description(self):
        description = "Описание компании. " * 200
        self.assertFalse(companies.validate_description(description))

    def test_digit_description(self):
        description = "12345678"
        self.assertFalse(companies.validate_description(description))

    def test_description(self):
        description = "краткое описание. Очень интересное и подробное описание."
        self.assertFalse(companies.validate_description(description))

if __name__ == '__main__':
    unittest.main()
