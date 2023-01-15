class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        b = bin(n)[2:][::-1]
        diff = 32 - len(b)
        b += "0" * diff
        print(b)
        return int(b,2)
        