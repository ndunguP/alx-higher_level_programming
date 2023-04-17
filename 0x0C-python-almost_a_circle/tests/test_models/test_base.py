<<<<<<< HEAD
#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

'''
    Creating test cases for the base module
'''


class test_base(unittest.TestCase):
    '''
        Testing base
    '''
    def test_id_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            Sending a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
            Sending an id 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            Sending a negative id
        '''
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        '''
            Sending an id that is not an int
        '''
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        '''
            Sending an id that is not an int
        '''
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        '''
            Sending an id that is not an int
        '''
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        '''
            Sending an id that is not an int
        '''
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        '''
            Testing the json string
        '''
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """
    class for testing Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
=======
"""Unittest for base.py"""
"""
Import unittest, Base class, and Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Base(unittest.TestCase):
    """Test for Base class
    Set up and Teardown
    """
    @classmethod
    def setUpClass(cls):
        """Setup environment"""
        cls.b1 = Base(1)
        cls.b2 = Base()
        cls.b3 = Base(None)
        cls.b4 = Base(35)
        cls.b5 = Base(5)
        cls.b6 = Base("name")
        cls.b7 = Base(2.25)
        cls.b8 = Base(-3.35)
        cls.b9 = Base(True)
        cls.b10 = Base(False)
        cls.b11 = Base([1, 2])
        cls.b12 = Base((1, 2))
        cls.b13 = Base({"name": "Carl"})
        cls.b14 = Base([])
        cls.b15 = Base(float('inf'))
        cls.b16 = Base(float('NaN'))

    @classmethod
    def tearDown(cls):
        """Tear down environment"""
        pass
    """
    Part 1: Test Base class
    Test 1.0
    """
    def test_case1_0(self):
        """Test for base type"""
        self.assertIsInstance(self.b1, Base)
    """
    Part 2: Test for id
    Test 2.0
    """
    def test_case2_0(self):
        """Test base id"""
        self.assertEqual(self.b2.id, 1)
        self.assertEqual(self.b3.id, 2)
        self.assertNotEqual(self.b4.id, 25)
    """
    Test 2.1
    """
    def test_case2_1(self):
        """Test base id with None"""
        self.assertEqual(self.b3.id, 2)
    """
    Test 2.2
    """
    def test_case2_2(self):
        """Test base id with integer"""
        self.assertEqual(self.b5.id, 5)
    """
    Test 2.3
    """
    def test_case2_3(self):
        """Test base id with string"""
        self.assertEqual(self.b6.id, "name")
    """
    Test 2.4
    """
    def test_case2_4(self):
        """Test base id with float"""
        self.assertEqual(self.b7.id, 2.25)
        self.assertEqual(self.b8.id, -3.35)
    """
    Test 2.5
    """
    def test_case2_5(self):
        """Test base id with True"""
        self.assertEqual(self.b9.id, True)
    """
    Test 2.6
    """
    def test_case2_6(self):
        """Test base id with False"""
        self.assertEqual(self.b10.id, False)
    """
    Test 2.7
    """
    def test_case2_7(self):
        """Test base id with list"""
        self.assertEqual(self.b11.id, [1, 2])
    """
    Test 2.8
    """
    def test_case2_8(self):
        """Test base id with tuple"""
        self.assertEqual(self.b12.id, (1, 2))
    """
    Test 2.9
    """
    def test_case2_9(self):
        """Test base id with dictionary"""
        self.assertEqual(self.b13.id, {"name": "Carl"})
    """
    Test 2.10
    """
    def test_case2_10(self):
        """Test Base id with empty list"""
        self.assertEqual(self.b14.id, [])
    """
    Test 2.11
    """
    def test_case2_11(self):
        """Test base id with nan and inf"""
        self.assertEqual(float('inf'), self.b15.id)
        self.assertNotEqual(float('NaN'), self.b16.id)
    """
    Test 2.12
    """
    def test_case2_12(self):
        """Test base id with empty argument"""
        self.assertEqual(self.b2.id, 1)
    """
    Test 2.13
    """
    def test_case2_13(self):
        """Test base id with too many arguments"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)
    """
    Test 2.14
    """
    def test_case2_14(self):
        """Test for error cases"""
        with self.assertRaises(ValueError):
            b = Base(int("hello"))
        with self.assertRaises(ValueError):
            b = Base(float("lazers"))
    """
    Part 3: JSON
    Test 3.0
    """
    def test_case3_0(self):
        """Test for to_json_string method in Base class"""
        r1 = Rectangle(1, 2, 3, 4)
        r_dict = r1.to_dictionary()
        j_dict = Base.to_json_string([r_dict])
        print(r_dict)
        self.assertEqual(type(r_dict), dict)
        print(j_dict)
        self.assertEqual(type(j_dict), str)
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
    """
    Test 3.1
    """
    def test_case3_1(self):
        """Test for save_to_file method in Base class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertIsInstance(r1, Base)
        try:
            with open("Rectangle.json", "r") as file:
                print(file.read())
        except Exception as e:
            print("{}".format(e))
        Rectangle.save_to_file(None)
        try:
            with open("rectangle.json", "r") as file:
                print(file.read())
        except Exception as e:
            print("{}".format(e))
        try:
            Rectangle.save_to_file()
        except Exception as e:
            print("{}".format(e))
    """
    Test 3.2
    """
    def test_case3_2(self):
        """Test for from_json_string method in Base class"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])
        l_in = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        j_in = Rectangle.to_json_string(l_in)
        l_out = Rectangle.from_json_string(j_in)
        self.assertEqual(type(l_in), list)
        self.assertEqual(type(j_in), str)
        self.assertEqual(type(l_out), list)
    """
    Test 3.3
    """
    def test_case3_3(self):
        """Test case for create method in Base class"""
        r3 = Rectangle(3, 5, 1, 1, 1)
        r1_d = r3.to_dictionary()
        rr = Rectangle.create(**r1_d)
        self.assertEqual(r3.__str__(), "[Rectangle] (1) 1/1 - 3/5")
        self.assertEqual(rr.__str__(), "[Rectangle] (1) 1/1 - 3/5")
        self.assertFalse(r3 is rr)
        self.assertFalse(r3 == rr)
        try:
            Rectangle.create("hello")
        except Exception as e:
            print("{}".format(e))
        try:
            Rectanlge.create()
        except Exception as e:
            print("{}".format(e))
        try:
            Rectangle.create("hi")
        except Exception as e:
            print("{}".format(e))
    """
    Test 3.4
    """
#    def test_case3_4(self):
 #       """Test for load_from_file method in Base class"""

if __name__ == "__main__":
    unittest.main()
>>>>>>> cadc0c7b075a8bc1a507ba5ffef0cacf06386ff5
