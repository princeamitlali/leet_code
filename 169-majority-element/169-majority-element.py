from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter
        threshold = len(nums)//2 
        dic  = c(nums)
        for i in dic:
            if dic[i] > threshold:
                return i
                