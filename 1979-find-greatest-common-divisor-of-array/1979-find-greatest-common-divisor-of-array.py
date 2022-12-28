class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        first,second = nums[-1],nums[0]
        while first != second:
            if first > second:
                first = first - second
            else:
                second = second - first
        return first
        # for i in range(s,0,-1):
        #     if l % i == 0 and s % i == 0:
        #         return i
        # return 1
        