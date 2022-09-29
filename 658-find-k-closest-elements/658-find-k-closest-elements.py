class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []
        for i in arr:
            temp.append([abs(i-x),i])
        temp = sorted(temp)
        res = []
        for i in range(k):
            res.append(temp[i][1])
        return sorted(res)
            
            
        # if x < min(arr):
        #     ind = 0
        # elif x > max(arr):
        #     ind = len(arr) -1
        # elif 
        # print(ind)
        # if ind == len(arr)-1:
        #     return arr[-k:]
        # if ind == 0:
        #     return arr[:k]
        # temp = []
        # l = ind -1
        # r = ind 
        # while k > 0 :
        #     if r > len(arr) -1 or l<0:
        #         break
        #     if arr[ind] - arr[l] <= arr[r] - arr[ind]:
        #         temp.insert(0,arr[l])
        #         l -= 1
        #         k -= 1
        #     else:
        #         temp.append(arr[r])
        #         r += 1
        #         k -= 1
        # print(l,r,k,temp)
        # if k > 0:
        #     if l == -1:
        #         for i in range(k):
        #             temp.append(arr[r+i])
        #     else:
        #         for i in range(k):
        #             temp.insert(0,arr[l-i])
        # return temp