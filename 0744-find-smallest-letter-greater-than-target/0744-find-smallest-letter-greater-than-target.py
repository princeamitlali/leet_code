class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        letters.sort()
        for i in letters:
            if i > target:
                return i 
        return res
        