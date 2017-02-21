import pytest


@pytest.fixture
def r():
    from Assignment1.retirement import Retirement
    return Retirement()


def test_hello_world(r):
    assert r.hello_world() == "hello world"
