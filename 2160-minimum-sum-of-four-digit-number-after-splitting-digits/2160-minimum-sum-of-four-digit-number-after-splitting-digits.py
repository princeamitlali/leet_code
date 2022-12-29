class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num))
        v1 = int(num[0]+num[-1])
        v2 = int(num[1]+num[2])
        return v1 + v2
        