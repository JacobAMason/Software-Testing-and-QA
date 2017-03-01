import pytest


@pytest.fixture
def em():
    from Assignment1.email_verifier import EmailVerifier
    return EmailVerifier


def test_valid_standard_email(em):
    assert em.is_valid_email("jacob@jacobmason.net")


def test_missing_at_symbol(em):
    assert not em.is_valid_email("jacobjacobmason.net")


def test_missing_period(em):
    assert not em.is_valid_email("jacob@jacobmasonnet")


def test_no_username(em):
    assert not em.is_valid_email("@jacobmason.net")


def test_no_domain_name(em):
    assert not em.is_valid_email("jacob@.net")


def test_no_tld(em):
    assert not em.is_valid_email("jacob@jacobmason.")


def test_period_separated_username(em):
    assert em.is_valid_email("jacob.mason@jacobmason.net")


def test_period_only_username(em):
    assert not em.is_valid_email(".@jacobmason.net")


def test_multiple_subdomains(em):
    assert em.is_valid_email("jacob@jacobmason.net.edu")


def test_period_only_subdomain(em):
    assert not em.is_valid_email("jacob@.")


def test_email_with_numerals(em):
    assert em.is_valid_email("j4c0b@j4c0bm4s0n.n3t")


def test_empty_string(em):
    assert not em.is_valid_email("")


def test_non_string(em):
    assert not em.is_valid_email(42)


def test_accepts_1_to_3_character_tlds(em):
    assert em.is_valid_email("jacob@jacobmason.valid.n")
    assert em.is_valid_email("jacob@jacobmason.valid.net")
    assert not em.is_valid_email("jacob@jacobmason.notv.alid")
