# Order of execution of the Test methods
import unittest
import inspect


class TestClass02(unittest.TestCase):

        def test_case02(self):
                print("\nRunning Test method : " + inspect.stack()[0][3])

        def test_case01(self):
                print("\nRunning Test method : " + inspect.stack()[0][3])


if __name__ == '__main__':
        unittest.main(verbosity=2)
