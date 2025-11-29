class Solution:
    def scoreOfString(self, s: str) -> int:
        c = 0
        for i in range(1,len(s)):
            c += abs(ord(s[i-1]) - ord(s[i]))
            # print(c)
        return c
        