class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        seats.sort()
        students.sort()
        for i in zip(seats,students):
            
            v = i[0] - i[1]
            res += abs(v)
        return res
                
        