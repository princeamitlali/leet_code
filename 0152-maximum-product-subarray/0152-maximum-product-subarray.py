class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        max_ending_here = arr[0]
        min_ending_here = arr[0]
        max_so_far = arr[0]
        for i in range(1, len(arr)):
            temp = max(max(arr[i], arr[i] * max_ending_here),
                       arr[i] * min_ending_here)
            min_ending_here = min(
                min(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
            max_ending_here = temp
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

        