class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        v = word.index(ch)
        return word[:v+1][::-1] + word[v+1:]
        