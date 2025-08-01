class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def count_partition(arr,k,max_sum):
            partition = 1
            sub_sum = 0

            for i in arr:
                if sub_sum + i <= max_sum :
                    sub_sum += i
                else:
                    sub_sum = i
                    partition += 1

            return partition

        if k > len(nums):
            return -1

        low = max(nums)
        high = sum(nums)
        
        while low <= high:
            mid = (low + high ) // 2

            if count_partition(nums,k,mid) > k :
                low = mid +1
            else:
                high = mid -1

        return low
        