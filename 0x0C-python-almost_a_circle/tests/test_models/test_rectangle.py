# test_rectangle.py

import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class.
    """

    def test_constructor(self):
        """
        Test case to verify the constructor initializes attributes correctly.
        """
        rect = Rectangle(10, 15, 3, 4, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 1)

    def test_getters_and_setters(self):
        """
        Test case to verify getters and setters work correctly.
        """
        rect = Rectangle(10, 15, 3, 4, 1)
        rect.width = 15
        rect.height = 25
        rect.x = 5
        rect.y = 6
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 6)


if __name__ == '__main__':
    unittest.main()
