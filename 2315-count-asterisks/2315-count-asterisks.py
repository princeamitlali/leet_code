class Solution:
    def countAsterisks(self, s: str) -> int:
        l = s.split("|")
        count = 0
        for i in range(0,len(l),2):
            for j in l[i]:
                if j == "*":
                    count += 1
        return count
    
        