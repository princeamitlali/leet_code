class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        val = ""
        for i in words:
            val += i [0]
        return val == s
        