from django.test import TestCase
from app.handler.trie import TrieAutocomplete


class TrieTest(TestCase):
    def setUp(self):
        self.trie = TrieAutocomplete()
        self.trie.insert("Michael Jordan", 1)
        self.trie.insert("Magic Johnson", 2)

    def test_suggestions(self):
        result = self.trie.get_suggestions("M")

        # Check that the result contains the correct dictionaries
        self.assertIn({'id': 1, 'name': 'Michael Jordan'}, result)
        self.assertIn({'id': 2, 'name': 'Magic Johnson'}, result)
