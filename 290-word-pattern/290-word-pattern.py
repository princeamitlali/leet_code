class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        val = s.split(" ")
        
        
        if len(val) != len(pattern):
            return False 
        def check(p,v):
            dic = {}
            for i in range(len(p)):
                if p[i] not in dic.keys():
                    dic[p[i]] = v[i]
                else:
                    if dic[p[i]] != v[i]:
                           return False 
            return True
        return True and check(pattern,val) and check(val,pattern)
        