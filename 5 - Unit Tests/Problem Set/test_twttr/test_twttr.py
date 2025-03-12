from twttr import shorten

def test_mixed():
    assert shorten("HellO, World") == "Hll, Wrld"

def test_all_caps():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"

def test_all_lower():
    assert shorten("hello, world") == "hll, wrld"

def test_numbers():
    assert shorten("123") == "123"
