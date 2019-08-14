# addfinalizer() finction
import pytest


@pytest.fixture()
def fixture01(request):
        print("\nIn fixture...")

        def fin():
            print("\nFinalized...")
        request.addfinalizer(fin)


@pytest.mark.usefixtures('fixture01')
def test_case01():
        print("\nIn test_case01()...")


