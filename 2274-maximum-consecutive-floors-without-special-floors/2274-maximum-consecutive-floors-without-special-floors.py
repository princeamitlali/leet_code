class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        special.insert(0,bottom-1)
        special.append(top+1)
        special = list(set(special))
        special.sort()
        # 
        res = 0
        print(special)
        for i in range(len(special)-1):
            res = max(res,(special[i+1] - special[i])-1)
        return res
        