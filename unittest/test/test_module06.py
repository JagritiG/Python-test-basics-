# Run the test module without unittest.main()
import unittest


class TestClass07(unittest.TestCase):

        def test_case01(self):
                self.assertTrue("PYTHON".isupper())
                print("\nIn test_case01()")
