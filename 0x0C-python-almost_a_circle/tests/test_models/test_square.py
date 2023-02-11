"""Unittest for Square class"""

"""
Import unittest
Import Square class
Import io
Import sys
"""
import unittest
from models.square import Square
import io
import sys

class Test_Square(unittest.TestCase):
    """Class to test class Square"""

    @classmethod
    def setUpClass(cls):
        """"""
        cls.s1 = Square(5, 6, 7, 8)
        cls.s2 = Square(1, 2, 3, 4)
        cls.s3 = Square(5)

    @classmethod
    def tearDownClass(cls):
        """Tear down"""
        pass

    """
    Part 1: Square
    """
    def test_case_0(self):
        """Test Square class"""
        self.assertTrue(type(self.s1), Square)
        self.assertIsInstance(self.s1, Square)

    """
    Test 1.0
    """
    def test_case1_0(self):
        """Test for attributes in Square class"""
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 6)
        self.assertEqual(self.s1.y, 7)
        self.assertEqual(self.s1.id, 8)
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(TypeError):
            s = Square("string")
        with self.assertRaises(TypeError):
            s = Square((1, 2))
        with self.assertRaises(TypeError):
            s = Square([])
        with self.assertRaises(TypeError):
            s = Square({'a': 5})
        with self.assertRaises(TypeError):
            s = Square(None)
        with self.assertRaises(TypeError):
            s = Square(True)
        with self.assertRaises(TypeError):
            s = Square(False)
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(4.45)
        with self.assertRaises(TypeError):
            s = Square(-4.45)
        with self.assertRaises(TypeError):
            s = Square(float('inf'))
        with self.assertRaises(TypeError):
            s = Square(float('NaN'))
    """
    Test 1.1
    """
    def test_case1_1(self):
        """Test case for update method in Square class"""
        self.s2.size = 25
        self.assertEqual(self.s2.size, 25)
        self.assertEqual(self.s2._Rectangle__width, 25)
        self.assertEqual(self.s2._Rectangle__height, 25)
        self.assertEqual(self.s2.x, 2)
        self.s2.update(x=12)
        self.assertEqual(self.s2.x, 12)
        self.s2.update(size=33)
        self.assertEqual(self.s2._Rectangle__width, 33)
        self.assertEqual(self.s2._Rectangle__height, 33)

    """
    Test 1.2
    """
    def test_case1_2(self):
        """Test case for print square in Square class"""
        output = io.StringIO()
        sys.stdout = output
        self.s3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#####\n" * 5)
        output = io.StringIO()
        sys.stdout = output
        print(self.s3)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (16) 0/0 - 5\n")
    """
    Test 1.3
    """
    def test_case1_3(self):
        """Test update method in Square class"""
        self.s3.update(10)
        self.assertEqual(self.s3.__str__(), "[Square] (10) 0/0 - 5")
        self.s3.update(1, 2)
        self.assertEqual(self.s3.__str__(), "[Square] (1) 0/0 - 2")
        self.s3.update(1, 2, 3)
        self.assertEqual(self.s3.__str__(), "[Square] (1) 3/0 - 2")
        self.s3.update(1, 2, 3, 4)
        self.assertEqual(self.s3.__str__(), "[Square] (1) 3/4 - 2")
        self.s3.update(x=12)
        self.assertEqual(self.s3.__str__(), "[Square] (1) 12/4 - 2")
        self.s3.update(size=7, y=1)
        self.assertEqual(self.s3.__str__(), "[Square] (1) 12/1 - 7")
        self.s3.update(size=7, id=89, y=1)
        self.assertEqual(self.s3.__str__(), "[Square] (89) 12/1 - 7")

if __name__ == "__main__":
    unittest.main()
