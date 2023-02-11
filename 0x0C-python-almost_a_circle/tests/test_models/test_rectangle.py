"""Unittest for Rectangle class"""
"""
Import unittest
Import Rectangle class
Import io
Import sys
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys

class TestRectangle(unittest.TestCase):
    """Test for rectangle class"""

    @classmethod
    def setUpClass(cls):
        """Set up environment"""
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(1, 2, 3, 4, 5)
        cls.r3 = Rectangle(2, 10)
        cls.r4 = Rectangle(8, 7, 0, 0, 12)
        cls.r5 = Rectangle(5, 3)
        cls.r6 = Rectangle(2, 3, 2, 2)
        cls.r7 = Rectangle(10, 10, 10, 10, 1)
        cls.r8 = Rectangle(10, 10, 10, 10, 1)
        cls.r9 = Rectangle (10, 2, 3, 9)
        cls.r10 = Rectangle(1, 1)

    @classmethod
    def tearDownClass(cls):
        """Tear down environment"""
        pass

    """Part 1: test class instance
    Test 1.0
    """
    def test_case1_0(self):
        """Test class instance"""
        self.assertIsInstance(self.r1, Rectangle)
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)

    """
    Part 2: test instance attrubte values
    Test 2.0
    """
    def test_case2_0(self):
        """Test positive attributes"""
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r2.y, 4)
        self.assertEqual(self.r2.id, 5)
    """
    Test 2.1
    """
    def test_case2_1(self):
        """Test value errors for attributes"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 3, 4, 5)
    """
    Test 2.2
    """
    def test_case2_2(self):
        """Test type errors for attributes"""
        with self.assertRaises(TypeError):
            r = Rectangle("value", 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, "value", 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "value", 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "value", 5)
        with self.assertRaises(TypeError):
            r = Rectangle([1, 2], 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, {'value':2}, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, (3, 4), 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, None, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(3.35, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, float("NaN"), 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, float("inf"), 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, {}, 5)
        a = "[TypeError] height must be an integer"
        b = "[ValueError] width must be > 0"
        c = "[TypeError] x must be an integer"
        d = "[ValueError] y must be >= 0"
        try:
            Rectangle(10, "2")
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e), a)
        try:
            r = Rectangle(10, 2)
            r.width = -10
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e), b)
        try:
            r = Rectangle(10, 2)
            r.x = {}
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e), c)
        try:
            Rectangle(10, 2, 3, -1)
        except Exception as e:
            self.assertEqual("[{}] {}".format(e.__class__.__name__, e), d)
    """
    Test 2.3
    """
    def test_case2_3(self):
        """Test for area method in Rectangle class"""
        print(self.r2.area())
        self.assertEqual(self.r2.area(), 2)
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r3.area(), 20)
        self.assertEqual(self.r4.area(), 56)
    """
    Test 2.4
    """
    def test_case2_4(self):
        """Test for display method in Rectangle class"""
        output = io.StringIO()
        sys.stdout = output
        self.r5.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#####\n" * 3)
        self.r5.display()
        self.assertEqual(output.getvalue(), "#####\n" * 3)
        output = io.StringIO()
        sys.stdout = output
        self.r6.display()
        sys.stdout = sys.__stdout__
        string = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output.getvalue(), string)
    """
    Test 2.5
    """
    def test_case2_5(self):
        """Test for string method in Rectangle class"""
        self.assertEqual(self.r2.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        output = io.StringIO()
        sys.stdout = output
        print(self.r2.__str__())
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (5) 3/4 - 1/2\n")
    """
    Test 2.6
    """
    def test_case2_6(self):
        """Test for update method in Rectangle class"""
        self.assertEqual(self.r7.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        output = io.StringIO()
        sys.stdout = output
        print(self.r7.__str__())
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        self.r7.update(89)
        self.assertEqual(self.r7.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        self.r7.update(89, 2)
        self.assertEqual(self.r7.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        self.r7.update(89, 2, 3)
        self.assertEqual(self.r7.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        self.r7.update(89, 2, 3, 4)
        self.assertEqual(self.r7.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        self.r7.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r7.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        self.r7.update(89, 2, 3, 4, 5)
        output = io.StringIO()
        sys.stdout = output
        print(self.r7.__str__())
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

        self.assertEqual(self.r8.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        self.r8.update(height=1)
        self.assertEqual(self.r8.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        self.r8.update(width=1, x=2)
        self.assertEqual(self.r8.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        self.r8.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.r8.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        self.r8.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r8.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    """
    Test 2.7
    """
    def test_case2_7(self):
        """Test for to_dictionary method in Rectangle class"""
        d = self.r9.to_dictionary()
        self.assertEqual(type(d), dict)
        self.r10.update(**d)
        self.assertEqual(self.r10.__str__(), "[Rectangle] (11) 3/9 - 10/2")
        r = Rectangle(3, 2, 1, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)
        with self.assertRaises(TypeError):
            r.to_dictionary("hi")
        with self.assertRaises(TypeError):
            r.to_dictionary(None)
if __name__ == "__main__":
    unittest.main()
