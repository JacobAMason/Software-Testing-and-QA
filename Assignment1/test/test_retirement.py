import pytest
from Assignment1.retirement import year_can_retire


def test_actually_works():
    assert year_can_retire(35, 100000, .1, 500000) == 60


def test_return_one_hundred_if_too_old():
    assert year_can_retire(40, 40000, .1, 500000) == 100


def test_should_throw_error_with_negative_age():
    with pytest.raises(ValueError):
        year_can_retire(-10, 1, 0, 0)


def test_should_throw_error_with_salary_zero_or_less():
    with pytest.raises(ValueError):
        year_can_retire(10, 0, 0, 0)


def test_should_throw_error_with_negative_savings():
    with pytest.raises(ValueError):
        year_can_retire(10, 1, -1, 0)


def test_should_throw_error_with_negative_goal():
    with pytest.raises(ValueError):
        year_can_retire(0, 1, 0, -1)


def test_should_throw_error_with_savings_larger_than_one():
    with pytest.raises(ValueError):
        year_can_retire(0, 1, 2, 1)


def test_should_raise_error_when_age_is_not_a_number():
    with pytest.raises(ValueError):
        year_can_retire("0", 1, 1, 1)


def test_should_raise_error_when_salary_is_not_a_number():
    with pytest.raises(ValueError):
        year_can_retire(0, "1", 1, 1)


def test_should_raise_error_when_saving_is_not_a_number():
    with pytest.raises(ValueError):
        year_can_retire(0, 1, "1", 1)


def test_should_raise_error_when_goal_is_not_a_number():
    with pytest.raises(ValueError):
        year_can_retire(0, 1, 1, "1")
