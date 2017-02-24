import pytest
from Assignment1.retirement import year_can_retire


class TestFunctionality():

    def test_actually_works(self):
        assert year_can_retire(35, 100000, .1, 500000) == 60

    def test_should_return_age_if_goal_is_zero(self):
        assert year_can_retire(30, 1, 1, 0) == 30

    def test_return_one_hundred_if_too_old(self):
        assert year_can_retire(40, 40000, .1, 500000) == 100

    def test_should_return_hundred_if_goal_is_positive_and_salary_is_0(self):
        assert year_can_retire(40, 0, 1, 1) == 100

    def test_should_return_hundred_if_goal_is_positive_and_saving_is_0(self):
        assert year_can_retire(40, 1, 0, 1) == 100


class TestBoundaries():

    def test_should_throw_error_with_negative_age(self):
        with pytest.raises(ValueError):
            year_can_retire(-10, 1, 0, 0)

    def test_should_throw_error_with_neagtive_salary(self):
        with pytest.raises(ValueError):
            year_can_retire(10, -1, 0, 0)

    def test_should_throw_error_with_negative_savings(self):
        with pytest.raises(ValueError):
            year_can_retire(10, 1, -1, 0)

    def test_should_throw_error_with_negative_goal(self):
        with pytest.raises(ValueError):
            year_can_retire(0, 1, 0, -1)

    def test_should_throw_error_with_savings_larger_than_one(self):
        with pytest.raises(ValueError):
            year_can_retire(0, 1, 2, 1)


class TestValidateInputType():

    def test_should_raise_error_when_age_is_not_a_number(self):
        with pytest.raises(ValueError):
            year_can_retire("0", 1, 1, 1)

    def test_should_raise_error_when_salary_is_not_a_number(self):
        with pytest.raises(ValueError):
            year_can_retire(0, "1", 1, 1)

    def test_should_raise_error_when_saving_is_not_a_number(self):
        with pytest.raises(ValueError):
            year_can_retire(0, 1, "1", 1)

    def test_should_raise_error_when_goal_is_not_a_number(self):
        with pytest.raises(ValueError):
            year_can_retire(0, 1, 1, "1")
