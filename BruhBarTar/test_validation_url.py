import re
import unittest
import companies

class ValidateLogoUrlTestCase(unittest.TestCase):
    def test_valid_url(self):
        url = "https://example.com/logo.png"
        self.assertTrue(companies.validate_logo_url(url))

    def test_invalid_url(self):
        url = "ftp://example.com/logo.png"
        self.assertFalse(companies.validate_logo_url(url))

    def test_invalid_url_without_scheme(self):
        url = "example.com/logo.png"
        self.assertFalse(companies.validate_logo_url(url))

    def test_invalid_url_with_spaces(self):
        url = "https://example.com /logo.png" 
        self.assertFalse(companies.validate_logo_url(url))

    def test_invalid_url_with_special_characters(self):
        url = "https://logos-marcas.com/wp-content/uploads/2020/09/National-Geographic-Channel-Logotipo-1997-2001.jpg"
        self.assertTrue(companies.validate_logo_url(url))

if __name__ == '__main__':
    unittest.main()
