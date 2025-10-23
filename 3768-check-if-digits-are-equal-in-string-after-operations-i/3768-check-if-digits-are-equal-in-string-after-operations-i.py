class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            tmp = ""
            for i in range(len(s)-1):
                x = int(s[i]) + int(s[i+1])
                x = x % 10
                tmp += str(x)
            s = tmp


        return s[0] == s[1]

        