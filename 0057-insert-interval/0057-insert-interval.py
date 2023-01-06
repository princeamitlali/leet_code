class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        res = [intervals[0]]
        for i in intervals[1:]:
            v = res[-1]
            if i[0] <= v[1]:
                res.pop()
                i
                res.append([min(i[0],v[0]),max(v[1],i[1])])
            else:
                res.append(i)
        print(res)
        return res
        