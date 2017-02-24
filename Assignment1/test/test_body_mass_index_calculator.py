import pytest


@pytest.fixture
def bmi():
    from Assignment1.body_mass_index_calculator import BodyMassIndexCalculator
    return BodyMassIndexCalculator


def test_convert_lbs_to_kgs(bmi):
    assert bmi.convert_lbs_to_kgs(125) == 56.25


def test_convert_height_inches(bmi):
    assert bmi.convert_height_to_inches(5, 3) == 63


def test_convert_height_meters(bmi):
    assert bmi.convert_inches_to_meters(63) == pytest.approx(1.575, rel=1e-2)


def test_bmi_calculation(bmi):
    assert bmi.calculate_bmi(63, 125) == pytest.approx(22.7, rel=1e-2)


def test_bmi_category_normal(bmi):
    assert bmi.determine_bmi_category(22.7) == "Normal"


def test_bmi_category_underweight(bmi):
    assert bmi.determine_bmi_category(18) == "Underweight"


def test_bmi_category_overweight(bmi):
    assert bmi.determine_bmi_category(28) == "Overweight"


def test_overweight_lower_bound(bmi):
    assert bmi.determine_bmi_category(25) == "Overweight"


def test_underweight_upper_bound(bmi):
    assert bmi.determine_bmi_category(18.4) == "Underweight"


def test_normal_weight_lower_bound(bmi):
    assert bmi.determine_bmi_category(18.5) == "Normal"


def test_normal_weight_upper_bound(bmi):
    assert bmi.determine_bmi_category(24.9) == "Normal"
