class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        v = bin(n)[2:][::-1]
        for i in range(len(v)):
            if v[i] == "1":
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even,odd]
        