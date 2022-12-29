class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1] 
        if len(s) == 1:
            return False
        for i in range(1,len(s)):
            cs = s
            cs = cs.replace(s[:i],"")
            if cs == "":
                return True
        return False
            
        