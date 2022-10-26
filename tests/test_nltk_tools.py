from src.nltk_tools import NltkTools
import sys
import unittest

sys.path.append("..")


class NltkToolsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.nl_tools = NltkTools()
        cls.sentence = "test sentence"
        cls.bag = cls.nl_tools.bag_of_words(
            cls.nl_tools.tokenize(cls.sentence), ["test", "test", "tes"]
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.nl_tools = None
        cls.sentence = None
        cls.bag = None

    def test_tokenize_words_separation_from_sentence(self):
        tokenized_sentence = self.nl_tools.tokenize(self.sentence)
        self.assertIn(tokenized_sentence[0], self.sentence)
        self.assertTrue(len(tokenized_sentence) == 2)

    def test_tokenize_if_returns_list_of_strings(self):
        tokenized_sentence = self.nl_tools.tokenize(self.sentence)
        self.assertIsInstance(tokenized_sentence[0], str)
        self.assertIsInstance(tokenized_sentence, list)

    def test_bag_of_words_return_list_of_floats(self):
        self.assertTrue(type(self.bag), list)
        self.assertIsInstance(self.bag[0], float)

    def test_bag_of_words_if_word_found_in_stemmed_sentence(self):
        self.assertTrue(self.bag[0] == 1.0)
        self.assertTrue(self.bag[1] == 1.0)
        self.assertTrue(self.bag[2] == 0)


if __name__ == "__main__":
    unittest.main()
