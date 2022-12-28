class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word2) > len(word1):
            n = len(word1)
            res = word2[n:]
        else:
            n = len(word2)
            res = word1[n:]
        d = ""
        for i in range(n):
            d += word1[i] + word2[i]
        return d+res
            
        