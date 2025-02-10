from app.dbmodels.models import Player  # Import Django model

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.player_id = None  # Store player ID when the word ends
        self.player_name = None  # Store original player name when the word ends


class TrieAutocomplete:
    def __init__(self):
        self.root = TrieNode()
        self.build_trie()  # Populate Trie with player names from database

    def build_trie(self):
        """Build the Trie using player names and IDs from the database"""
        player_data = Player.objects.values('player_id', 'name')  # Fetch both player_id and name
        for player in player_data:
            self.insert(player['name'], player['player_id'])

    def insert(self, name, player_id):
        """Insert a word into the Trie and associate it with player_id"""
        node = self.root
        for char in name.lower():  # Convert to lowercase only for the Trie structure
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.player_id = player_id  # Store player_id when a word ends
        node.player_name = name  # Store original player name with proper capitalization

    def get_suggestions(self, prefix):
        """Get autocomplete suggestions based on the prefix"""
        node = self.root
        # Convert prefix to lowercase for case-insensitive search
        for char in prefix.lower():
            if char not in node.children:
                return []  # No suggestions if prefix not in Trie
            node = node.children[char]

        # Perform DFS from the node that matches the prefix to get all suggestions
        return self._dfs(node)

    def _dfs(self, node):
        """Perform DFS to collect all words and return both player_id and name"""
        suggestions = []
        if node.is_end_of_word:
            # Append a dictionary containing the player ID and original name (with proper capitalization)
            suggestions.append({"id": node.player_id, "name": node.player_name})

        # Continue DFS to find all child nodes
        for char, child_node in node.children.items():
            suggestions.extend(self._dfs(child_node))

        return suggestions
