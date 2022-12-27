class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            s = str(bin(i)).split("b")[-1]
            count = 0
            for j in s:
                if j == "1":
                    count += 1
            res.append(count)
            
        # print(str(bin(n)).split("b")[-1])
        return res
        