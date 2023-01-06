class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        res = []
        while len(res) < k:
            if i not in arr:
                res.append(i)
            i += 1
        print(res)
        return res[-1]
        