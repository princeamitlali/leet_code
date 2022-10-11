class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ra = [nums[0]]
        for i in nums:
            ra.append(min(ra[-1],i))
        la = [nums[-1]]
        for i in nums[::-1]:
            la.append(max(la[-1],i))
        la = la[::-1]
        for i in range(len(nums)):
            if ra[i] < nums[i] < la[i]:
                return True
        return False
        