class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def num_of_sub_arrays(k,nums):
            l=r=cnt = 0
            mapp= {}
            while r < len(nums):
                mapp[nums[r]] = mapp.get(nums[r],0) + 1
                # print(mapp)
                while len(mapp) > k :
                    mapp[nums[l]] = mapp[nums[l]] - 1

                    if mapp[nums[l]] == 0:
                        del mapp[nums[l]]
                    l +=1
                cnt += r-l+1
                r += 1
            return cnt

        return num_of_sub_arrays(k,nums) - num_of_sub_arrays(k-1,nums)
        