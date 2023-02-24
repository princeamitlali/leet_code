class Solution:
    def digitSum(self, s: str, k: int) -> str:
        i = 0
        while len(s) > k:
            i = 0
            temp = ""
            j =0
            while j < len(s):
                temp += str(sum(int(i) for i in s[j : j+k]))
                j += k
            
            s = temp
        return s