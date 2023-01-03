import math
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda item: (str(bin(item))[2:].count("1"), item))