# @pytest.mark.usefixtures() decorator is used for a class
import pytest


@pytest.fixture()
def fixture01():
        print("\nIn fixture01()...")


@pytest.mark.usefixtures('fixture01')
class TestClass03:
        def test_case01(self):
                print("\nIn the test_case01")

        def test_case02(self):
                print("\nIn the test_case02")

