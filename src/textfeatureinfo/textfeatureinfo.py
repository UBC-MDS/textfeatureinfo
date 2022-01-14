# Count number of punctuations
def count_punc(text):
    """
    Counts the number of punctuations within the text.
    
    Parameters:
    ___________
    text: (str)
    piece of text to analyze

    Returns:
    ___________
    
    Integer
    the number of punctuations
    

    Examples
    ________
    >>> count_punc("Hello, World!")
    2
    >>> count_punc("Hello World")
    0
    """
    
# Average count length
def avg_word_len(text):
    """
    Calculates the average length of the words within the text.

    Parameters:
    ___________
    text: (str)
    piece of text to analyze

    Returns
    _______
    the average length of words within the text

    Examples
    ________
    >>> avg_word_len("Hello, World!")
    """

# Count percentage of fully capitalised words
def perc_cap_words(text):
    """
    Calculate percentage of fully capitalised words in the text.
   
    Parameters:
    ------
    text: (str)
    the input text
    
    Returns:
    -------
    percentage of capitalised words: float
    """

# Remove stopwords
def remove_stop_words(text, language="english"):
    """
    Removes stop words from the text and returns the list of clear words in the text.

    Parameters:
    ------
    text (str): The text that you want to remove stop words from.
    language (str, optional): The language of the text. Defaults to 'english'.

    Returns:
    ------
    list: The list of the words in the text that are not stop words.

    Examples:
    ------
    >>> remove_stop_words("Tomorrow is a big day!")
    ['tomorrow', 'big', 'day!']
    """
