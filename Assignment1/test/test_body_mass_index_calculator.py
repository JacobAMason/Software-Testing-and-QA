import pytest


@pytest.fixture
def bmi():
    from Assignment1.body_mass_index_calculator import BodyMassIndexCalculator
    return BodyMassIndexCalculator()


def test_convert_weight(bmi):
    assert bmi.convert_weight(125) == 56.25


def test_convert_height_inches(bmi):
    assert bmi.convert_height_inches(5, 3) == 63


# approx is used for floating point tolerance
def test_convert_height_metric(bmi):
    assert bmi.convert_height_metric(63) == pytest.approx(1.575, rel=1e-2)


# approx is used to ensure floating point calculations are
# correct to within 2 decimal places from example in doc
def test_bmi_calculation(bmi):
    assert bmi.calculate_bmi(63, 125) == pytest.approx(22.7, rel=1e-2)


def test_bmi_category_normal(bmi):
    assert bmi.determine_bmi_category(22.7) == "Normal"


def test_bmi_category_underweight(bmi):
    assert bmi.determine_bmi_category(18.4) == "Underweight"


def test_bmi_category_overweight(bmi):
    assert bmi.determine_bmi_category(25) == "Overweight"
