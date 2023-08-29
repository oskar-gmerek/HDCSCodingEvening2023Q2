import unittest
from unittest.mock import patch
from color_converter import rgbToHex

class TestRGBtoHex(unittest.TestCase):

    def test_rgb_to_hex(self):
        self.assertEqual(rgbToHex(255,255,255), '#FFFFFF')
        self.assertEqual(rgbToHex(66,135,245), '#4287F5')
        self.assertEqual(rgbToHex(145,12,56), '#910C38')
        self.assertEqual(rgbToHex(101,105,135), '#656987')
        self.assertEqual(rgbToHex(0,0,0), '#000000')

    def test_wrong_rgb_input(self):
        self.assertIsNone(rgbToHex(333,333,333))
        self.assertIsNone(rgbToHex(-1,333,333))

if __name__ == '__main__':
    unittest.main()