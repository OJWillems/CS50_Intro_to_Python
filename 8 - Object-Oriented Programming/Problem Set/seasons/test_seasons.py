import pytest
from datetime import date, timedelta
from seasons import user_date_input_validation, get_minute_differential, minute_phrase_parser

def test_input_validation():
    assert user_date_input_validation("2024-02-27") == {"year": 2024, "month": 2, "day": 27}
    assert user_date_input_validation("2024-12-05") == {"year": 2024, "month": 12, "day": 5}
    with pytest.raises(SystemExit):
        user_date_input_validation("February 27, 2024")

def test_get_minute_differential():
    yesterday = date.today() - timedelta(days=1)
    tomorrow = date.today() + timedelta(days=1)
    assert get_minute_differential({"year": yesterday.year, "month": yesterday.month, "day": yesterday.day}) == 24 * 60
    with pytest.raises(SystemExit):
        get_minute_differential({"year": tomorrow.year, "month": tomorrow.month, "day": tomorrow.day})

def test_minute_phrase_parser():
    assert minute_phrase_parser(1) == "One" 
    assert minute_phrase_parser(50) == "Fifty"
    assert minute_phrase_parser(525600) == "Five hundred twenty-five thousand, six hundred"