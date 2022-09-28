class Solution:
    def isIsomorphic(self, p: str, v: str) -> bool:
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
        