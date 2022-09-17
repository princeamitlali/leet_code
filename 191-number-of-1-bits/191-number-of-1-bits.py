class Solution:
    def hammingWeight(self, n: int) -> int:
        st = bin(n)
        st = st.replace("0b","")
        st = st.replace("0","")
        return len(st)
        