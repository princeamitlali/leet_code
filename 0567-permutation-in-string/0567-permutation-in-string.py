class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        # print(s1)
        m = len(s1)
        for i in range(len(s2)-m+1):
            v = s2[i:i+m]
            v = sorted(v)
            # print(v)
            if v == s1:
                return True
            
        return False