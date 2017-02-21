import pytest


@pytest.fixture
def bmi():
    from Assignment1.body_mass_index import BodyMassIndex
    return BodyMassIndex()


def test_hello_world(bmi):
    assert bmi.hello_world() == "hello world"
