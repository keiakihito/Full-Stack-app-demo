# autocomplete_handler.py
from app.handler.trie import TrieAutocomplete

class AutocompleteHandler:
    def __init__(self):
        self.trie = TrieAutocomplete()

    def get_player_suggestions(self, query):
        """
        Fetch autocomplete suggestions for the given query.
        This method interacts with the TrieAutocomplete class to get player name suggestions.
        """
        return self.trie.get_suggestions(query)
