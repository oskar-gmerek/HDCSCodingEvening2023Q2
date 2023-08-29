import unittest
from unittest.mock import patch
from color_converter import rgbToHex, rgbToCmyk

class TestRGBtoHex(unittest.TestCase):

    # Test if results are correct
    def test_rgb_to_hex(self):
        self.assertEqual(rgbToHex(255,255,255), '#FFFFFF')
        self.assertEqual(rgbToHex(66,135,245), '#4287F5')
        self.assertEqual(rgbToHex(145,12,56), '#910C38')
        self.assertEqual(rgbToHex(101,105,135), '#656987')
        self.assertEqual(rgbToHex(0,0,0), '#000000')

    # Test if result is none when wrong rgb input is provided
    def test_wrong_rgb_input(self):
        self.assertIsNone(rgbToHex(333,333,333))
        self.assertIsNone(rgbToHex(-1,333,333))


class TestRGBtoCmyk(unittest.TestCase):

    # Test if results are correct
    def test_rgb_to_cmyk(self):
        self.assertEqual(rgbToCmyk(255,255,255), 'cmyk(0%,0%,0%,0%)')
        self.assertEqual(rgbToCmyk(66,135,245), 'cmyk(73%,45%,0%,4%)')
        self.assertEqual(rgbToCmyk(145,12,56), 'cmyk(0%,92%,61%,43%)')
        self.assertEqual(rgbToCmyk(101,105,135), 'cmyk(25%,22%,0%,47%)')
        self.assertEqual(rgbToCmyk(0,0,0), 'cmyk(0%,0%,0%,100%)')

    # Test if result is none when wrong rgb input is provided
    def test_wrong_rgb_input(self):
        self.assertIsNone(rgbToCmyk(333,333,333))
        self.assertIsNone(rgbToCmyk(-1,333,333))

if __name__ == '__main__':
    unittest.main()