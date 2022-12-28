class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        c = 0
        for word in words:
            if pref == word[:n]:
                c += 1
        return c
        