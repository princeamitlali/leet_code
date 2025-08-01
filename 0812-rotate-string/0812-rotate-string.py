class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s_new =  s[i:] + s[:i]
            # print(s_new)
            if s_new == goal:
                return True

        return False
        

     
        