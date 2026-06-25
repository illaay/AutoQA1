from odd import EvenOddChecker
import pytest


@pytest.fixture
def fixture():
    return EvenOddChecker()


def test_is_even(fixture):
    assert fixture.is_even(2) is True
    assert fixture.is_even(3) is False
    assert fixture.is_even(-2) is True


def test_is_odd(fixture):
    assert fixture.is_odd(2) is False
    assert fixture.is_odd(3) is True
    assert fixture.is_odd(-2) is False
