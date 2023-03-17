class Trie:

    def __init__(self):
        self.main = defaultdict(int)
        self.sub = defaultdict(int)
        

    def insert(self, word: str) -> None:
        self.main[word] = 0
        for i in range(len(word)):
            self.sub[word[:i+1]] = 0
        

    def search(self, word: str) -> bool:
        return word in self.main
        
        
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.sub
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)