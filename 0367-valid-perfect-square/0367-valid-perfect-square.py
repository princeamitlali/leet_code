class Solution:
    def isPerfectSquare(self, val: int) -> bool:
        ans = 0
        start = 0
        end = val

        while end >= start:
            mid = (end + start) //2
            mid_sq = mid * mid
            if mid_sq == val:
                return mid
            elif mid_sq > val:
                end = mid -1
            else:
                start = mid + 1
                ans = mid
        return ans * ans == val
        