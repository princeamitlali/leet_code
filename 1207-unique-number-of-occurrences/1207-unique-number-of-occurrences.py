from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        val = Counter(arr)
        # val = c(arr)
        t = []
        for i in val:
            t.append(val[i])
        return len(t) == len(set(t))

        