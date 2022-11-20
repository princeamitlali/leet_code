class Solution:
    
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(s):
            s = list(s)
            while "#" in s:
                # print(s)
                ind = s.index("#")
                if ind == 0:
                    s.pop(ind)
                else:
                    s.pop(ind-1)
                    s.pop(ind-1)
                # print(s)
            return "".join(s)
        # print(remove(s), remove(t))
        return remove(s) == remove(t)
        
            
        