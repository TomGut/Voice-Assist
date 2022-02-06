import nltk
import numpy as np
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

_stemmer = PorterStemmer()


class Nltk_Tools():

    def tokenize(self, sentence):
        return nltk.word_tokenize(sentence)

    def stem(self, word):
        return _stemmer.stem(word.lower())

    def bag_of_words(self, tokenized_sentence, all_words):
        tokenized_sentence = [self.stem(w) for w in tokenized_sentence]
        bag = np.zeros(len(all_words), dtype=np.float)
        for idx, w in enumerate(all_words):
            if w in tokenized_sentence:
                bag[idx] = 1.0
        return bag
