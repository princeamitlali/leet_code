from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        val = Counter(arr)
        
        val = sorted(val.items() , key = lambda kv:kv[1],reverse = True)
        count = 0 
        c = len(arr)
        last = len(val)
        for key,value in val:
            c -= value
            count += 1
            if c <= len(arr) //2:
                break
                
        return count