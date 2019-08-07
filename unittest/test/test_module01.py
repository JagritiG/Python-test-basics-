import unittest


# Create test class
class TestClass01(unittest.TestCase):

        # Class methods
        def test_case01(self):
                my_str = "TestPythonCode"
                my_int = 121
                # Assertion method which check if the argument
                # passed to it is True or false
                self.assertTrue(isinstance(my_str, str))
                self.assertTrue(isinstance(my_int, int))

        def test_case02(self):
                my_pi = 3.14
                self.assertFalse(isinstance(my_pi, int))


# Test Runner
if __name__ == '__main__':
        unittest.main()



