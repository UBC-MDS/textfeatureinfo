from textfeatureinfo.textfeatureinfo import remove_stop_words
from nltk.corpus import stopwords
import pytest

def test_remove_stop_words():
    """
    To check whether remove_stop_words()) works as designed.
    
    3 tests in total.
    """   
    text1 = "We cannot solve our problems with the same thinking we used when we created them."
    text2 = "!!!"
    text3 = "UBC MDS is an amazing program!"
    assert remove_stop_words(text1) == ['cannot', 'solve', 'problems', 'thinking', 'used', 'created', 'them.'], "The stop words are not removed correctly!"
    assert remove_stop_words(text2) == ['!!!']. "The stop words are not removed correctly!"
    assert remove_stop_words(text3) == ['ubc', 'mds', 'amazing', 'program!'], "The stop words are not removed correctly!"


def test_remove_stop_words_error():
    """Check TypeError raised when the text is empty or the language does not exist."""
     with pytest.raises(TypeError):
        text1 = ""
        remove_stop_words(text1)

    with pytest.raises(TypeError):
        text2 = 2
        remove_stop_words(text2)
    
    with pytest.raises(TypeError):
        text3 = 'Hello'
        remove_stop_words(text2, text2)