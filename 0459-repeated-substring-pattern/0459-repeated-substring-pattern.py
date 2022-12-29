class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        for i in range(1,len(s)):
            cs = s
            cs = cs.replace(s[:i],"")
            if cs == "":
                return True
        return False
            
        