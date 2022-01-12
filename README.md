# textfeatureinfo

This python package includes functions assisting data scientists to extract information from text features that can be useful in their data science projects. The four-in-one simple tool will help gather summary information from plain text such as the number of punctuations appeared, the average word lengths, count the percentage of fully capitalised words  and also to manipulate text data by removing the stopwords for the ease of future processing steps. 

Our package and functions are inspired from a lab of 573 (Feature and model selection) course of UBC MDS program, and are tailored based on our own experience and interest. 

In the field of text feature engineering, we are cognisant that there are well established packages in the Python ecosystem - specifically `nltk`, `SpaCy` and `genism`. For punctuations, we are aware that the `nltk.tokenize` and `nltk.probability: FreqDist` that can be used to find the number of words and punctuations in a string [https://www.nltk.org/api/nltk.tokenize.html]. To calculate average word length,`nltk.word_tokenize()` is able to divide strings into lists of substrings, . To count the number of fully capitalised words in a text, the above functions do provide a means to isolate these characters, but not to count them explicitly. In the case of stop words, there are several modules that identify stop words. For instance, `genius.parsing.preprocessing` module has the function `remove_stopwords()` which allows users to remove specific stop words, as listed in their docstring from a string. `nltk.corpus` has a module `stopwords` to remove stop wards from the `text_token` list. The package `SpaCy` similarly has a list of stopwords stored in `sp.Default.stop_words` in English. 

Based on our experience in our previous module, all the functions that we seek to use require several lines of code. For example, to calculate the average word length, we need to extract the punctuation, count total number of characters, then averaging out over the number of words present. As such, we seek to simplify these tasks into functions that users, including ourselves, can employ in one line of code. 

References (*To be moved to the reference section*): 
https://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_extraction.text
https://stackabuse.com/removing-stop-words-from-strings-in-python/#usingthespacylibrary
https://stackoverflow.com/questions/14500028/extracting-most-frequent-words-out-of-a-corpus-with-python

## Installation

```bash
$ pip install textfeatureinfo
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`textfeatureinfo` was created by Kiran, Jacqueline, Paniz, Lynn. It is licensed under the terms of the MIT license.

## Credits

`textfeatureinfo` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
