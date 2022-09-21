class Solution(object):
    def threeSumClosest(self, nums, target):
        diff = sys.maxsize
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            low = i + 1
            high = n-1
            while low < high:
                su = nums[i] + nums[low] + nums[high]
                if target == su :
                    return target
                if su > target:
                    high -= 1
                else:
                    low +=1
                if abs(target -su) < diff:
                    ans = su
                    diff = abs(target-su)
        return ans
        