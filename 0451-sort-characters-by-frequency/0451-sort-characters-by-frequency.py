from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
        st = ''
        for key,val in freq:
            st += key* val
        return st
        
        