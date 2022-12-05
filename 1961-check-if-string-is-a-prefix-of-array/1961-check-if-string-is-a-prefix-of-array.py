class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s2 = ""
        for i in words:
            s2 += i
            if s2 == s:
                return True
        return False
        