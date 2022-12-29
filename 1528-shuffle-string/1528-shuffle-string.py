class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0 for i in range(len(indices))]
        
        for i in zip(s,indices):
            res[i[1]] = i[0]
        return "".join(res)