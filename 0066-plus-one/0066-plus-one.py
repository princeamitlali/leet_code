class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = str(int("".join(map(str,digits))) + 1 )
        digits = []
        for i in val:
            digits.append(int(i))

        return digits
        