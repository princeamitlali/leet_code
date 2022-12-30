class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c = 0
        for i in zip(startTime,endTime):
            if i[0] <= queryTime <= i[1]:
                c += 1
        return c
        