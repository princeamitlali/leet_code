class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        sol = [intervals[0]]

        for i,j in intervals:
            if i <= sol[-1][1]:
                sol[-1][1] = max(sol[-1][1],j)
            else:
                sol.append([i,j])
        return sol
        