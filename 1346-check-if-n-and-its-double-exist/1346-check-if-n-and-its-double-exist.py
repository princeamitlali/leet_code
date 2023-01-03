class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            if 2 * arr[i]  in arr[i+1:] or 2 * arr[i] in arr[:i]:
                return True
            
        return False
        