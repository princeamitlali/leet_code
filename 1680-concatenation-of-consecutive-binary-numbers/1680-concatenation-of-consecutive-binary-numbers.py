class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # return int("".join([str(bin(i))[2:] for i in range(1,n+1)]),2)%(10**9+7)
        temp = ""
        for i in range(1,n+1):
            temp += bin(i)[2:]
        return int(temp,2) % (10**9 + 7)
        