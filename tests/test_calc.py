import pytest
from src.calc import add, subtruct, multiply, divide

def test_add():
    assert add(3, 1) == 4
    assert add(5, 6) == 11
    assert add(7, 8) == 15


def test_substruct():
    assert subtruct(3, 8) == -5
    assert subtruct (1, 4) == -3
    assert subtruct(5, 1) == 4


def test_multipy():
    assert multiply(1, 3) == 3
    assert multiply(5, 6) == 30
    assert multiply(8, 9) == 72


def test_divide():
    assert divide(4, 2) == 2
    assert divide(8, 4) == 2
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(6, 0)