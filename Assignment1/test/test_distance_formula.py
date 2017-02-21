import pytest


@pytest.fixture
def df():
    from Assignment1.distance_formula import DistanceFormula
    return DistanceFormula()


def test_hello_world(df):
    assert df.hello_world() == "hello world"
