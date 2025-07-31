class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1,-1,-1):
            if num[i] in ["1","3","5","7","9"]:
                return num[:i+1]

        return ""