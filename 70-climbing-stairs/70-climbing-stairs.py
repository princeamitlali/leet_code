class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        for i in range(n):
            temp = second
            second += first
            first = temp
        return second