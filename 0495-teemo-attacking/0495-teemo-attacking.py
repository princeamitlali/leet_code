class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        diff = 0
        for i in range(1,len(timeSeries)):
            if timeSeries[i-1] + duration > timeSeries[i]:
                diff += (timeSeries[i-1] + duration) - timeSeries[i]
            print(diff)
        return (len(timeSeries) * duration) - diff
            
        
        