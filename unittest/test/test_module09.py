# test module for mypackage
from mypackage.mymathlib import *
import unittest

math_obj = 0


def setUpModule():
        """called once, before anything else in the module"""
        print("In setUpModule()...")
        global math_obj
        math_obj = mymathlib()


def tearDownModule():
        """called once, after anything else in the module"""
        print("In tearDownModule()...")
        global math_obj
        del math_obj


class TestClass10(unittest.TestCase):

            @classmethod
            def setupClass(cls):
                    """called only once, before any test in the class"""
                    print("In setUpClass()...")

            def setUp(self):
                    """Called once, before every test method"""
                    print("\nIn setUp()...")

            def test_case01(self):
                    print("In test_case01()")
                    self.assertEqual(math_obj.add(2, 6), 8)

            def test_case02(self):
                    print("In test_case02()")

            def tearDowm(self):
                    """Called once, after every test method"""
                    print("\nIn tearDowm()...")

            @classmethod
            def tearDownClass(cls):
                    """called only once, after all the tests in the class"""
                    print("In tearDownClass()...")

