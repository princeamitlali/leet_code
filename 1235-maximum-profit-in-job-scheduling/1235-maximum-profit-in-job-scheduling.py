class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs, dp = [], [0] * (len(startTime) + 1)
        for e, s, p in zip(endTime, startTime, profit): jobs.append((e, s, p))
        jobs.sort()
        dp[1] = jobs[0][2]
        for i in range(1, len(jobs)):
            dp[i + 1] = max(dp[bisect_right(jobs, jobs[i][1], key=lambda x: x[0])] + jobs[i][2], dp[i])
        return dp[-1]
        