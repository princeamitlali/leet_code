class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        for i in nums:
            temp.append(i)
        for i in nums:
            temp.append(i)
        return temp
        