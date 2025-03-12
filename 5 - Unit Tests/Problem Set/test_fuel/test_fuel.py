from fuel import convert, gauge
import pytest

def test_convert_integers():
    convert("1/2") == 50
    convert("1/3") == 33

def test_convert_numerator_greater_denominator():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_denominator_zero():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_convert_non_integer_num_or_den():
    with pytest.raises(ValueError):
        convert("a/b")

def test_gauge_full():
    assert gauge(99) == "F"

def test_gauge_empty():
    assert gauge(1) == "E"

def test_gauge_normal():
    assert gauge(33) == "33%"
