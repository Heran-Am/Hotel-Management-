import unittest
import getinfoui  # Importing your module

class TestGetInfoUI(unittest.TestCase):
    def test_import(self):
        # Check if the module is imported successfully
        self.assertIsNotNone(getinfoui)

    def test_hotel_management_class_exists(self):
        # Check if the HOTEL_MANAGEMENT class exists in the imported module
        self.assertTrue(hasattr(getinfoui, 'HotelManagementApp'))

if __name__ == '__main__':
    unittest.main()

