class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = nums[0]
        end = nums[0]
        res = []
        for i in nums:
            print(start,end,i)
            if i-end > 1:
                if start != end:
                    res.append(str(start)+"->"+str(end))
                else:
                    res.append(str(start))
                start = i
                end = i
            else:
                end = i
            
        if start != end:
            res.append(str(start)+"->"+str(end))
        else:
            res.append(str(start))
        return res
        