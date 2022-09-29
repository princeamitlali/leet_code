class Solution(object):
    def maxSubArray(self, li):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = li[0]
        max_end = li[0]
        for i in range(1,len(li)):
            max_end = max(li[i],max_end + li[i])
            res = max(res,max_end)
        return res
        