# id() returns the name of the method and
# shortDescription() returns the description of the method.
import unittest


class TestClass11(unittest.TestCase):

        def test_case01(self):
                """This is a test method"""
                print("\nIn test_case01()")
                print(self.id())
                print(self.shortDescription())

