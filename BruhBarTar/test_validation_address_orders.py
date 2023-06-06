import unittest
import orders

class AddressValidationTestCase(unittest.TestCase):
    def test_valid_address(self):
        address = "��. ����������� 1, �. �����, �. 5"
        result = orders.validate_address(address)
        self.assertTrue(result)

    def test_valid_address_with_extra_elements(self):
        address = "��. ����������� 1, �. �����, �. 5, ��. 10"
        result = orders.validate_address(address)
        self.assertTrue(result)

    def test_valid_address_with_additional_spaces(self):
        address = "   ��. �����������   1,   �. �����,   �. 5   "
        result = orders.validate_address(address)
        self.assertTrue(result)

    def test_valid_address_with_different_casing(self):
        address = "��. ����������� 1, �. �����, �. 5"
        result = orders.validate_address(address)
        self.assertTrue(result)

    def test_valid_address_with_missing_elements(self):
        address = "��. ����������� 1, �. �����"
        result = orders.validate_address(address)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
