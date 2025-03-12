import pytest
from bank import value # type: ignore

def test_hello():
    assert value("hello") == "$0"
    assert value("HELLO") == "$0"

def test_hey():
    assert value("hey") == "$20"
    assert value("HEY") == "$20"

def test_other():
    assert value("sup?") == "$100"
    assert value("SUP?") == "$100"

def test_int():
    with pytest.raises(AttributeError):
        value(1)