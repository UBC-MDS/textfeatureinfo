# Count number of punctuations
def count_punc(text):
    """
    Count the number of punctuations within the text.
    
    Parameters
    ----------
    text : str
        piece of text to analyze

    Returns
    -------
    integer
        the number of punctuations

    Examples
    --------
    >>> count_punc("Hello, World!")
    2
    >>> count_punc("Hello World")
    0
    """
    if not isinstance(s, str): 
        raise TypeError("Please enter a 'str' type.")
    count = 0
    for ch in s:
        if ch in punctuation:
            count += 1
    return count
    
# Average word length
# def avg_word_len(text):
    """
    Calculate the average length of the words within the text.

    Parameters
    ----------
    text : str
        piece of text to analyze

    Returns
    -------
    float
        the average length of words within the text

    Examples
    --------
    >>> avg_word_len("Hello, World!")
    5
    """

# Count percentage of fully capitalised words
# def perc_cap_words(text):
    """
    Calculate percentage of fully capitalised words in the text.

    Parameters
    ----------
    text : str
        the input text
    
    Returns
    -------
    float
        percentage of capitalised words
    
    Examples
    --------
    >>> perc_cap_words("THIS is a SPAm MESSage.")
    20%
    >>> perc_cap_words("THIS is a SPAM MESSAGE.")
    60%
    """

# Remove stopwords
# def remove_stop_words(text, language="english"):
    """
    Remove stop words from the text and return the list of clear words in the text.

    Parameters
    ----------
    text : str
        piece of text to analyze
    language : str (optional)
        the language of the text (default = 'english')

    Returns
    -------
    list
        the list of the words in the text that are not stop words.

    Examples
    --------
    >>> remove_stop_words("Tomorrow is a big day!")
    ['tomorrow', 'big', 'day!']
    """
