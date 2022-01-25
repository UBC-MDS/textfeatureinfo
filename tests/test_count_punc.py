import pytest
from textfeatureinfo.textfeatureinfo import count_punc

def test_count_punc():
    """
    To check whether count_punc() works as designed.
    
    3 tests in total.
    """   
    s = "\"['TEXT']\""
    s2 = '{}|,";'
    s3 = ''
    assert count_punc(s) == 6, "Output should be 6"
    assert count_punc(s2) == 6, "Output should be 6"
    assert count_punc(s3) == 0, "Output should be 0"


def test_count_punc_error():  
    """Check TypeError raised when string is not used."""
    with pytest.raises(TypeError):
        str_object = ["Some punctuations->!?{}[]"]
        count_punc(str_object)
        
    with pytest.raises(TypeError):
        str_object2 = 123456
        count_punc(str_object2)
