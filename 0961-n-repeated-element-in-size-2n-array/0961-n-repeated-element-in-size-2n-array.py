class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if dic.get(i,0) == 0:
                dic[i] = 1
            else:
                return i
        