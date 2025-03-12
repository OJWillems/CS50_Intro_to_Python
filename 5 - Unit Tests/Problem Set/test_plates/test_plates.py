import pytest
from plates import is_valid

def test_length():
    assert is_valid("a") == False
    assert is_valid("asdfghjk") == False
    assert is_valid("asdf") == True

def test_letter_start():
    assert is_valid("12as") == False
    assert is_valid("as12") == True

def test_numbers_at_the_end():
    assert is_valid("as12as") == False

def test_first_number_not_zero():
    assert is_valid("as01") == False
    assert is_valid("as10") == True

def test_no_periods_or_spaces_or_punctuation_marks():
    assert is_valid("as..") == False
    assert is_valid("as 2") == False