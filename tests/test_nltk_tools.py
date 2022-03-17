import sys
import unittest

sys.path.append("..")

from src.nltk_tools import Nltk_Tools


class Nltk_Tools_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.nl_tools = Nltk_Tools()
        cls.sentence = "test sentence"

    def test_tokenize_words_separation_from_sentence(self):
        tokenized_sentence = self.nl_tools.tokenize(self.sentence)
        self.assertIn(tokenized_sentence[0], self.sentence)
        self.assertTrue(len(tokenized_sentence) == 2)

    def test_tokenize_if_returns_list_of_strings(self):
        tokenized_sentence = self.nl_tools.tokenize(self.sentence)
        self.assertIsInstance(tokenized_sentence[0], str)
        self.assertIsInstance(tokenized_sentence, list)


if __name__ == "__main__":
    unittest.main()
