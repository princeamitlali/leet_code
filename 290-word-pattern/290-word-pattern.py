class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        v = s.split(" ")
        if len(set(p)) != len(set(v)):
            return False
        
        if len(v) != len(p):
            return False 
        dic = {}
        for i in range(len(p)):
            if p[i] not in dic.keys():
                dic[p[i]] = v[i]
            else:
                if dic[p[i]] != v[i]:
                       return False 
        return True
        # return True and check(pattern,val) and check(val,pattern)
        