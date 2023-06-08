import unittest
import Grisha

class DateValidationTest(unittest.TestCase):
    def test_valid_date(self):
        date = "2023-06-07"
        result = Grisha.checkDate(date)
        self.assertTrue(result)

    def test_invalid_non_date(self):
        date = ""
        result = Grisha.checkDate(date)
        self.assertFalse(result)

    def test_invalid_later_date(self):
        date = "2023-09-12"
        result = Grisha.checkDate(date)
        self.assertFalse(result)

    def test_invalid_earlier_date(self):
        date = "2023-01-01"
        result = Grisha.checkDate(date)
        self.assertFalse(result)
