from hello import hello # type: ignore

def test_argument():
    assert hello("Ollie") == "Hello, Ollie"

def test_default():
    assert hello() == "Hello, World"