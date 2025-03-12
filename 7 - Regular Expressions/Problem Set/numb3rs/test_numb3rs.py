import pytest
from numb3rs import validate

def correct_inputs():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_amount_of_numbers():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False

def test_periods():
    assert validate("1111") == False

def test_negative():
    assert validate("-1.-1.-1.-1") == False

def too_big():
    assert validate("1.1.1.256") == False
    assert validate("1.1.256.1") == False
    assert validate("1.256.1.1") == False
    assert validate("256.1.1.1") == False

def test_cs50():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False

def test_bs():
    assert validate('127.300.1.2') == False
    assert validate('127.1.300.2') == False
    assert validate('127.1.2.300') == False
    assert validate('127.300.300.300') == False