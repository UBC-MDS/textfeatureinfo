import pytest
from textfeatureinfo.textfeatureinfo import avg_word_len


def test_avg_word_len():
    """
    Tests the calculation of the average word length from a string.
    """
    s1 = ""
    s2 = "Hello World"
    s3 = "!!!hello!!!"
    s4 = "Here.are.some.words."
    s5 = "Hello, World!"

    assert avg_word_len(s1) == 0, "Output should be 0"
    assert avg_word_len(s2) == 5, "Output should be 5"
    assert avg_word_len(s3) == 5, "Output should be 5"
    assert avg_word_len(s4) == 4, "Output should be 4"
    assert avg_word_len(s5) == 5, "Output should be 5"


def test_avg_word_len_errors():
    """
    Checks for TypeErrors when the incorrect argument type is passed into avg_word_len.
    """
    with pytest.raises(TypeError):
        alist = ["a list of words"]
        avg_word_len(alist)

    with pytest.raises(TypeError):
        adict = {"a": "dictionary of words"}
        avg_word_len(adict)


test_avg_word_len()
