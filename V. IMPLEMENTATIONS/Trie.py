class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]

        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]

        return True


# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
