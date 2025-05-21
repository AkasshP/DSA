class Trie:

    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        self.trie[word] = word

    def search(self, word: str) -> bool:
        if self.trie.get(word):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for values in self.trie.values():
            if values.startswith(prefix):
                return True
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)