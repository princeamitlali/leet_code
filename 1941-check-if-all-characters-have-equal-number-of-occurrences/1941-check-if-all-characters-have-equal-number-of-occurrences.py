from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        pre = freq[s[0]]

        for i in freq:
            if freq[i] != pre:
                return False
        return True
            