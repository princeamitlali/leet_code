import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = "^" + p + "$"
        return re.search(p,s)