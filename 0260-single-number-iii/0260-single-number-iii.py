class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor1 = 0
        for i in nums:
            xor1 ^= i
        
        lowestBit = xor1 & (-xor1)
        res = [0]*2
        for i in range(n):
            if(lowestBit & nums[i] == 0):
                res[0] ^= nums[i]
            else:
                res[1] ^= nums[i]
        
        return res
        