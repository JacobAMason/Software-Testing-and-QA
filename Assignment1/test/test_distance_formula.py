import pytest


@pytest.fixture
def df():
    from Assignment1.distance_formula import DistanceFormulaCalculator
    return DistanceFormulaCalculator


def test_distance_is_0(df):
    assert df.compute_distance(0, 0, 0, 0) == 0


def test_distance_is_1_x_axis_only(df):
    assert df.compute_distance(2, 0, 1, 0) == 1


def test_distance_is_1_x_axis_only_neg_val(df):
    assert df.compute_distance(-2, 0, -1, 0) == 1


def test_distance_is_4_x_axis_only_pos_neg(df):
    assert df.compute_distance(2, 0, -2, 0) == 4


def test_distance_is_1_x_axis_only_0_to_1(df):
    assert df.compute_distance(0, 0, 1, 0) == 1


def test_distance_is_1_x_axis_only_1_to_0(df):
    assert df.compute_distance(1, 0, 0, 0) == 1


def test_distance_is_1_x_axis_only_0_to_neg_1(df):
    assert df.compute_distance(0, 0, -1, 0) == 1


def test_distance_is_1_x_axis_only_neg_1_to_0(df):
    assert df.compute_distance(-1, 0, 0, 0) == 1


def test_distance_is_1_y_axis_only(df):
    assert df.compute_distance(0, 2, 0, 1) == 1


def test_distance_is_1_y_axis_only_neg_val(df):
    assert df.compute_distance(0, -2, 0, -1) == 1


def test_distance_is_4_y_axis_only_pos_neg(df):
    assert df.compute_distance(0, 2, 0, -2) == 4


def test_distance_is_1_y_axis_only_0_to_1(df):
    assert df.compute_distance(0, 0, 0, 1) == 1


def test_distance_is_1_y_axis_only_1_to_0(df):
    assert df.compute_distance(0, 1, 0, 0) == 1


def test_distance_is_1_y_axis_only_0_to_neg_1(df):
    assert df.compute_distance(0, 0, 0, -1) == 1


def test_distance_is_1_y_axis_only_neg_1_to_0(df):
    assert df.compute_distance(0, -1, 0, 0) == 1


def test_distance_is_1_each_axis(df):
    # Difference of 1 on each axis should produce square root(2)overall
    assert df.compute_distance(2, 2, 1, 1) == pytest.approx(1.414213562)


def test_distance_is_1_each_axis_neg_val(df):
    # Difference of 1 on each axis should produce square root(2)overall
    assert df.compute_distance(-2, -2, -1, -1) == pytest.approx(1.414213562)


def test_distance_both_axes_extreme_x(df):
    # Extreme difference in x values should override the difference in y
    assert df.compute_distance(2, 0, 1000000000, 10) == pytest.approx(
        1000000000)


def test_distance_both_axes_extreme_y(df):
    # Extreme difference in y values should override the difference in x
    assert df.compute_distance(0, 0, 20, 1000000000) == pytest.approx(
        1000000000)


def test_distance_both_axes_shorter_than_1(df):
    assert df.compute_distance(0, 0, 0.3, 0.5) == pytest.approx(0.5830951895)


def test_non_number_input(df):
    with pytest.raises(TypeError, message="Values must be numbers"):
        df.compute_distance("a", "b", "c", "d")
