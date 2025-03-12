import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(TypeError):
        Jar("Hello")
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5


def test_sneaky_cookie_assignment():
    jar = Jar(5)
    jar.size = 2
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError):
        jar.size = 6
    with pytest.raises(ValueError):
        jar.size = -1    
    jar._size = 6
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.size = 1
    assert str(jar) == "🍪"
    jar.size = 12
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():
    jar = Jar(5)
    jar.size = 4
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.withdraw(2)