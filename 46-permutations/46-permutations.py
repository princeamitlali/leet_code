from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [i for i in permutations(nums)]
                
        