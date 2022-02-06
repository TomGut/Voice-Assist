import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

_stemmer = PorterStemmer()

class Nltk_Tools():

    def tokenize(self, sentence):
        return nltk.word_tokenize(sentence)


    def stem(self, word):
        return _stemmer.stem(word.lower())


    def bag_of_words(self, tokenized_sentence, all_words):
        pass
