import pytest
from simple_math import SimpleMath


@pytest.fixture
def simple_math():
    return SimpleMath()


@pytest.mark.parametrize("num, expected", [(3, 9), (0, 0)])
def test_square_int(simple_math, num, expected):
    assert simple_math.square(num) == expected


def test_square_float(simple_math):
    assert simple_math.square(1.5) == 2.25


@pytest.mark.parametrize("num, expected", [(3, 27), (0, 0)])
def test_cube_int(simple_math, num, expected):
    assert simple_math.cube(num) == expected


def test_cube_float(simple_math):
    assert simple_math.cube(1.5) == 3.375