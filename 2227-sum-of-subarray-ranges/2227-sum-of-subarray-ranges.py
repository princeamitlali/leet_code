
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        minsum = maxsum = 0

        stack = []
        for next_smaller in range(n + 1):
            print(stack)
            while stack and (next_smaller == n or nums[stack[-1]] > nums[next_smaller]):
                i = stack.pop()
                prev_smaller = stack[-1] if stack else -1
                minsum += nums[i] * (next_smaller - i) * (i - prev_smaller)
            stack.append(next_smaller)
        print(minsum)
        stack = []
        for next_larger in range(n + 1):
            print(stack)
            while stack and (next_larger == n or nums[stack[-1]] < nums[next_larger]):
                i = stack.pop()
                prev_larger = stack[-1] if stack else -1
                maxsum += nums[i] * (next_larger - i) * (i - prev_larger)
            stack.append(next_larger)
        
        return maxsum - minsum