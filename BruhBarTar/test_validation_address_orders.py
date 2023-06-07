import unittest
import orders

class AddressValidationTestCase(unittest.TestCase):
    def test_valid_address(self):
        address = "ул. Центральная 1, г. Город, д. 5"
        result = orders.validate_address(address)
        self.assertTrue(result)

    def test_valid_address_with_extra_elements(self):
        address = "ул. Центральная 1, г. Город, д. 5, оф. 10"
        result = orders.validate_address(address)
        self.assertTrue(result)

    def test_valid_address_with_additional_spaces(self):
        address = "   ул. Центральная   1,   г. Город,   д. 5    "
        result = orders.validate_address(address)
        self.assertTrue(result)

    def test_valid_address_with_different_casing(self):
        address = "УЛ. Центральная 1, г. Город, Д. 5"
        result = orders.validate_address(address)
        self.assertFalse(result)

    def test_valid_address_with_missing_elements(self):
        address = "ул. Центральная 1, г. Город"
        result = orders.validate_address(address)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
