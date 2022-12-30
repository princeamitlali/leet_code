class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum([abs(i[0] - i[1]) for i in zip(sorted(seats),sorted(students))])
        
                
        