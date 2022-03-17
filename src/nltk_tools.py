"""
Classification of words from user to match them to intents context by bag of 
words method. Word classification makes possible to choose which intent the sentnce 
belong to and match it with proper answer later on.
"""

from typing import Any, List

import nltk
import numpy as np
import numpy.typing as npt

# In case of missing Punkt Sentence Tokenizer uncomment line below.
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

_stemmer = PorterStemmer()


class Nltk_Tools:
    def tokenize(self, sentence: str) -> List[str]:
        """
        Separation of sentence into smaller units (tokens) to be classifed
        later on in bag of words.

        Args:
            sentence (str): text to be tokenized

        Returns:
            List[str]: tokenized sentence divided into single words
        """
        return nltk.word_tokenize(sentence)

    def stem(self, word: str) -> str:
        """
        Extraction of word base - removing affixes at the end of word.

        Args:
            word (str): word to be stemmed.

        Returns:
            str: stemmed word.
        """
        return _stemmer.stem(word.lower())

    def bag_of_words(
        self, tokenized_sentence: str, all_words: List[str]
    ) -> npt.NDArray[Any]:
        """
        Text Classification.
        Take all the words in sentence, then count the number of occurrences
        of each word.
        After finding the number of occurrences of each word, we will choose
        a certain number of words that appeared more often than other words.
        These words are the features for our classification problem.
        Then when it comes to classification, the classifier, will check what
        are the words and which intent they belong to later on.

        Args:
            tokenized_sentence (str): tokenized words
            all_words List[str]: all words to be put in the bag for classification

        Returns:
            numpy array: list of floats indicating if word exists in the
            sentence (1.0) or not (0) - words classification (match to pattern in intents).
        """
        tokenized_sentence = [self.stem(w) for w in tokenized_sentence]
        bag = np.zeros(len(all_words), dtype=float)
        for idx, w in enumerate(all_words):
            if w in tokenized_sentence:
                # Word classification in array to check if word shows in sentence.
                # 1 stands for - exist.
                bag[idx] = 1.0
        return bag
