# from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = sum(arr)
        m = len(arr) + 1
        n = 3
        while n < len(arr)+1:
            # print(n,m-n)
            for i in range(m-n):
                res += sum(arr[i:i+n])
            n += 2
        return res