from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(rem):

            if rem == 0:
                return 1

            partialRem = 0

            # Pick numbers from nums
            for num in nums:

                # Skip any number that reduce the remain to a negative number
                if rem - num < 0:
                    continue

                # Accumulate the number of combinations return from the remain (aka the target - a picked number) into the partial result
                partialRem += dp(rem - num)

            # Return the partial result
            return partialRem

        return dp(target)
        