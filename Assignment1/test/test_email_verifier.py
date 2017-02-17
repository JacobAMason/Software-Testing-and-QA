import pytest

@pytest.fixture
def em():
    from Assignment1.email_verifier import EmailVerifier
    return EmailVerifier()


def test_hello_world(em):
    assert em.hello_world() == "hello world"
