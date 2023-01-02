"""Unittest for max_integer([..])

"""

import unittest

max_integer = __import__('6-max_integer').max_integer





class TestMaxInteger(unittest.TestCase):

        """Class for testing max integer of a list"""

            def test_max_integer(self):

                        """Test max integer of a list"""

                                """

                                        SUCCESS

                                                """

                                                        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

                                                                self.assertEqual(max_integer([1, 88, 3, -6, -3]), 88)

                                                                        self.assertEqual(max_integer([-41, -32, -6, -4, -1]), -1)

                                                                                self.assertEqual(max_integer([99, 6, 43]), 99)

                                                                                        self.assertEqual(max_integer([44, 52, 13, 79, 12, 1098, 31]), 1098)

                                                                                                self.assertEqual(max_integer([]), None)

                                                                                                        self.assertEqual(max_integer(["cats", "hi"]), "hi")

                                                                                                                self.assertEqual(max_integer([5]), 5)



                                                                                                                        """

                                                                                                                                ERROR

                                                                                                                                        """

                                                                                                                                                with self.assertRaises(TypeError):

                                                                                                                                                                max_integer(4)

                                                                                                                                                                        with self.assertRaises(TypeError):

                                                                                                                                                                                        max_integer(["cats", 7])



                                                                                                                                                                                        if __name__ == "__main__":

                                                                                                                                                                                                unittest.main()
