import pytest
from convert import convert

def test_integer_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-3)

def test_error():
    with pytest.raises(TypeError):
        convert("cat")