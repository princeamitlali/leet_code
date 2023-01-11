class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        s_set = set(s)
        for i in s:
            val = ord(i)-97
            # idx = s.index(i)
            # idx2 = s[idx+1:].index(i)
            # print(idx2,idx)
            if distance[val] != s[s.index(i)+1:].index(i):
                return False
        return True
        