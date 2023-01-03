class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            v = nums[:i] + nums[i+1:]
            # print(v)
            if sorted(v) == v and len(set(v))==len(v):
                return True

        return False
        
            
        