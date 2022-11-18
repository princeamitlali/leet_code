class Solution:
    def countSegments(self, s: str) -> int:
        arr = s.split(" ")
        count = 0
        for i in arr:
            if i != "":
                count += 1
        return count
        