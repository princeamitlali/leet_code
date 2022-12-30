class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        for i in zip(sorted(seats),sorted(students)):
            res += abs(i[0] - i[1])
        return res
                
        