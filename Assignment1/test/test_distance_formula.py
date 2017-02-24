import pytest


@pytest.fixture
def df():
    from Assignment1.distance_formula import DistanceFormula
    return DistanceFormula(0, 0, 0, 0)


def test_hello_world(df):
    assert df.hello_world() == "hello world"


def test_distance_is_0(df):
    assert df.compute_distance() == 0
