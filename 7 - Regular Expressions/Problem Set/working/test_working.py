import pytest
from working import convert # type: ignore

def test_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"

def test_pm_to_am():
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("11 PM to 11 AM") == "23:00 to 11:00"

def test_minutes_included():
    assert convert("9:22 AM to 5:15 PM") == "09:22 to 17:15"
    assert convert("9:22 PM to 5:15 AM") == "21:22 to 05:15"

def test_minutes_included_and_not():
    assert convert("9 AM to 11:33 PM") == "09:00 to 23:33"
    assert convert("9:33 AM to 11 PM") == "09:33 to 23:00"

def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
        convert("Test Fail")
        convert("4:61 PM to 11 AM")
        convert("9 AM - 5 PM")

def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:15 AM to 12:15 PM") == "00:15 to 12:15"
    assert convert("12:15 PM to 12:15 AM") == "12:15 to 00:15"

def test_cs50():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")