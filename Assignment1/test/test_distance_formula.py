import pytest
from pytest import approx


@pytest.fixture
def df():
    from Assignment1.distance_formula import DistanceFormula
    return DistanceFormula(0, 0, 0, 0)


def test_hello_world(df):
    assert df.hello_world() == "hello world"


def test_distance_is_0(df):
    assert df.compute_distance() == approx(0)


def test_distance_is_1_x_axis_only(df):
    df.x1 = 2
    df.x2 = 1
    assert df.compute_distance() == approx(1)


def test_distance_is_1_y_axis_only(df):
    df.y1 = 2
    df.y2 = 1
    assert df.compute_distance() == approx(1)


def test_distance_is_1_each_axis(df):
    df.y1 = 2
    df.y2 = 1
    df.x1 = 2
    df.x2 = 1
    # Difference of 1 on each axis should produce square root(2)overall
    assert df.compute_distance() == approx(1.414213562)
