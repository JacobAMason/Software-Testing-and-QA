import pytest
from pytest import approx


@pytest.fixture
def bmi():
    from Assignment1.body_mass_index import BodyMassIndex
    return BodyMassIndex(5, 3, 125)


def test_convert_weight(bmi):
    assert bmi.convert_weight(bmi.weight) == 56.25


def test_convert_height_inches(bmi):
    assert bmi.convert_height_inches(bmi.feet, bmi.inches) == 63


# approx is used for floating point tolerance
def test_convert_height_metric(bmi):
    bmi.height_inches = bmi.convert_height_inches(bmi.feet, bmi.inches)
    assert bmi.convert_height_metric(bmi.height_inches) == approx(1.575)


# approx is used to ensure floating point calculations are
# correct to within 2 decimal places from example in doc
def test_bmi_calculation(bmi):
    bmi.height_inches = bmi.convert_height_inches(bmi.feet, bmi.inches)
    assert bmi.calculate_bmi(bmi.height_inches,
                             bmi.weight) == approx(22.7, rel=1e-2)


def test_bmi_category(bmi):
    # might have goofed this calcing bmi here isn't great
    bmi.height_inches = bmi.convert_height_inches(bmi.feet, bmi.inches)
    bmi.mass_index = bmi.calculate_bmi(bmi.height_inches, bmi.weight)
    assert bmi.determine_bmi_category(bmi.mass_index) == "Normal"
