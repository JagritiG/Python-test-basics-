# pytest Fixtures: @pytest.fixtuer decorator is used in the following test code
import pytest


@pytest.fixture()
def fixture01():
        print("\nIn fixture01()...")


def test_case01(fixture01):
        print("\nIn test_case01()...")


def test_case02(fixture01):
        print("\nIn test_case02()...")
