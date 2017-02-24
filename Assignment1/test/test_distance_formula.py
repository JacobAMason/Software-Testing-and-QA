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


def test_distance_is_1_x_axis_only_neg_val(df):
    df.x1 = -2
    df.x2 = -1
    assert df.compute_distance() == approx(1)


def test_distance_is_4_x_axis_only_pos_neg(df):
    df.x1 = 2
    df.x2 = -2
    assert df.compute_distance() == approx(4)


def test_distance_is_1_x_axis_only_0_to_1(df):
    df.x1 = 0
    df.x2 = 1
    assert df.compute_distance() == approx(1)


def test_distance_is_1_x_axis_only_1_to_0(df):
    df.x1 = 1
    df.x2 = 0
    assert df.compute_distance() == approx(1)


def test_distance_is_1_x_axis_only_0_to_neg_1(df):
    df.x1 = 0
    df.x2 = -1
    assert df.compute_distance() == approx(1)


def test_distance_is_1_x_axis_only_neg_1_to_0(df):
    df.x1 = -1
    df.x2 = 0
    assert df.compute_distance() == approx(1)


def test_distance_is_1_y_axis_only(df):
    df.y1 = 2
    df.y2 = 1
    assert df.compute_distance() == approx(1)


def test_distance_is_1_y_axis_only_neg_val(df):
    df.y1 = -2
    df.y2 = -1
    assert df.compute_distance() == approx(1)


def test_distance_is_4_y_axis_only_pos_neg(df):
    df.y1 = 2
    df.y2 = -2
    assert df.compute_distance() == approx(4)


def test_distance_is_1_y_axis_only_0_to_1(df):
    df.y1 = 0
    df.y2 = 1
    assert df.compute_distance() == approx(1)


def test_distance_is_1_y_axis_only_1_to_0(df):
    df.y1 = 1
    df.y2 = 0
    assert df.compute_distance() == approx(1)


def test_distance_is_1_y_axis_only_0_to_neg_1(df):
    df.y1 = 0
    df.y2 = -1
    assert df.compute_distance() == approx(1)


def test_distance_is_1_y_axis_only_neg_1_to_0(df):
    df.y1 = -1
    df.y2 = 0
    assert df.compute_distance() == approx(1)


def test_distance_is_1_each_axis(df):
    df.y1 = 2
    df.y2 = 1
    df.x1 = 2
    df.x2 = 1
    # Difference of 1 on each axis should produce square root(2)overall
    assert df.compute_distance() == approx(1.414213562)


def test_distance_is_1_each_axis_neg_val(df):
    df.y1 = -2
    df.y2 = -1
    df.x1 = -2
    df.x2 = -1
    # Difference of 1 on each axis should produce square root(2)overall
    assert df.compute_distance() == approx(1.414213562)


def test_distance_both_axes_extreme_x(df):
    df.y1 = 0
    df.y2 = 10
    df.x1 = 2
    df.x2 = 1000000000
    # Extreme difference in x values should override the difference in y
    assert df.compute_distance() == approx(1000000000)


def test_distance_both_axes_extreme_y(df):
    df.y1 = 0
    df.y2 = 1000000000
    df.x1 = 0
    df.x2 = 20
    # Extreme difference in y values should override the difference in x
    assert df.compute_distance() == approx(1000000000)


def test_distance_both_axes_shorter_than_1(df):
    df.y1 = 0
    df.y2 = 0.5
    df.x1 = 0
    df.x2 = 0.3
    assert df.compute_distance() == approx(0.5830951895)
