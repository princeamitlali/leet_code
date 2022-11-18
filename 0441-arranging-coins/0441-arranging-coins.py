class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        s = 0
        while s+count < n:
            count +=1
            s += count
            # print(s,count)
        # print(s+count,count)   

        return count
        