class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occurance(li,to_find):
    
            start = 0
            end = len(li) -1

            while end >= start:
                mid = (end + start ) //2
                if li[mid] < to_find:
                    start = mid + 1
                elif li[mid] > to_find:
                    end = mid -1
                else:
                    if mid == 0 or li[mid-1] != li[mid]:
                        return mid
                    else:
                        end = mid -1

            return -1
        def last_occurance(li,to_find):
    
            start = 0
            end = len(li) -1

            while end >= start:
                mid = (end + start ) //2
                if li[mid] < to_find:
                    start = mid + 1
                elif li[mid] > to_find:
                    end = mid -1
                else:
                    if mid == len(li) - 1 or li[mid+1] != li[mid]:
                        return mid
                    else:
                        start = mid +1

            return -1
        return [first_occurance(nums,target),last_occurance(nums,target)]
        