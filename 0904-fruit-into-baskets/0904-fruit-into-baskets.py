from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        
        # Pointers to keep track of subarray
        l, r = 0, 0
        
        # Max number of fruits that can be picked
        max_fruits = 0
        
        # Iterate through fruit array
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            
            # If there is more then 2 fruits
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
                
            max_fruits = max(max_fruits, r - l + 1)
            
        return max_fruits
#         if len(fruits) < 3 :
#             return len(fruits)
#         val = []
#         freq = []
#         fruits.append(-1)
#         count = 1
#         for i in range(len(fruits)-1):
#             if fruits[i+1] != fruits[i]:
#                 temp = 0
#                 if len(val) > 0 and val[-1] == fruits[i+1]:
#                     if fruits[i] == 0:
#                         temp = 0
#                     # print("in")
#                     else:
#                         temp = freq[-1] 
#                 freq.append(count)
#                 val.append(fruits[i])
#                 count = temp
#             count += 1
#             # print(fruits[i],count)
#         # print(freq)
#         if len(freq) == 1:
#             return freq[0]
#         m = -1
        
#         for i in range(len(freq)-1):
#             m = max(m,freq[i]+freq[i+1])
#         return m
    
            