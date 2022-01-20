import pytest
from textfeatureinfo.textfeatureinfo import perc_cap_words

def test_perc_cap_words():
    """
    To check whether perc_cap_words() works as designed.
    
    3 tests in total.
    """   
    s1 = 'THIS IS SPAM!'
    s2 = '1234 !!! oked'
    s3 = 'I have downloaded this package Before! YAHOO!'
    assert perc_cap_words(s1) == 100.0, "Output should be 100.0%"
    assert perc_cap_words(s2) == 0.0, "Output should be 0.0%"
    assert perc_cap_words(s3) == 28.57142857142857, "Output should be 28.57142857142857%"

def test_perc_cap_words_error():
    """Check TypeError raised when the text is empty or when string is not input."""
    with pytest.raises(TypeError):
        numbers = 123
        perc_cap_words(numbers)

    with pytest.raises(TypeError):
        blank = ''
        perc_cap_words(blank)