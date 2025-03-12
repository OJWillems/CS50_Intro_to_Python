import pytest
from um import count

def blank_string():
    assert count("") == 0

def um_alone():
    assert count("um") == 1

def um_punctuation():
    assert count("um)") == 1
    assert count("(um") == 1
    assert count("(um)") == 1

def um_capitalized():
    assert count("Um") == 1
    assert count("UM") == 1
    
def um_words():
    assert count("stump") == 0
    assert count("umpire") == 0
    assert count("drum") == 0

def um_sentences():
    assert count("Um, thanks for the album") == 1
    assert count("Umpire, um, I assume you play the drums with your, um, bum") == 2

def test_cs50():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

