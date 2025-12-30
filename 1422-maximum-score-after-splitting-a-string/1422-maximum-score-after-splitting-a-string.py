class Solution:
    def maxScore(self, s: str) -> int:
        sum_ones = 0
        for i in s:
            if i == '1':
                sum_ones += 1
        sum_zeros = 0
        val = 0
        for i in s[:-1]:
            if i == '0':
                sum_zeros += 1
            else:
                sum_ones -=1
            val = max(val,sum_zeros + sum_ones)
        return val