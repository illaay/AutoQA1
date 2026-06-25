import pytest

from age import AgeValidator


@pytest.fixture
def age_validator():
    return AgeValidator()


def test_is_adult(age_validator):
    assert age_validator.is_adult(18) is True
    assert age_validator.is_adult(19) is True


def test_is_not_adult(age_validator):
    assert age_validator.is_adult(0) is False
    assert age_validator.is_adult(17) is False


def test_is_not_adult_float(age_validator):
    assert age_validator.is_adult(17.99) is False