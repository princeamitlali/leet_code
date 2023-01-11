import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #approch 1 heap
        li = []
        for i in range(k):
            li.append( (abs(arr[i] -x),arr[i]))
        heapq.heapify(li)
        for i in arr[k:]:
            heapq.heappush(li,(abs(i-x),i))
        # print(li)
        res = []
        for i in range(k):
            v = heapq.heappop(li)
            res.append(v[1])
        return sorted(res)
        
        # approch 2 queue
        
#         queue = list()
#         for n in arr:
#             if len(queue) < k: queue.append(n)
#             else:
#                 if abs(n-x) < abs(queue[0]-x):
#                     queue.pop(0)
#                     queue.append(n)

#         return queue

# approch 3 naive

#         if x < min(arr):
#             ind = 0
#         elif x > max(arr):
#             ind = len(arr) -1
#         elif x not in arr:
#             temp = []
#             for i in arr:
#                 temp.append([abs(i-x),i])
#             temp = sorted(temp, key = lambda x : (x[0],x[1]))
#             print(temp)
#             res = []
#             for i in range(k):
#                 res.append(temp[i][1])
#             return sorted(res)
#         else:
#             ind = arr.index(x)
            
#         if ind == len(arr)-1:
#             return arr[-k:]
#         if ind == 0:
#             return arr[:k]
#         temp = []
#         l = ind -1
#         r = ind 
#         while k > 0 :
#             if r > len(arr) -1 or l<0:
#                 break
#             if arr[ind] - arr[l] <= arr[r] - arr[ind]:
#                 temp.insert(0,arr[l])
#                 l -= 1
#                 k -= 1
#             else:
#                 temp.append(arr[r])
#                 r += 1
#                 k -= 1
#         print(l,r,k,temp)
#         if k > 0:
#             if l == -1:
#                 for i in range(k):
#                     temp.append(arr[r+i])
#             else:
#                 for i in range(k):
#                     temp.insert(0,arr[l-i])
#         return temp