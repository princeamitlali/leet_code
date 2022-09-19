class Solution:
    def spiralOrder(self, li: List[List[int]]) -> List[int]:
        m = len(li)
        n = len(li[0])

        k = 0
        l = 0
        temp = []
        while (k < m and l < n):
            for i in range(l, n):
                temp.append(li[k][i])

            k += 1

            for i in range(k, m):
                temp.append(li[i][n - 1])

            n -= 1

            if (k < m):

                for i in range(n - 1, (l - 1), -1):
                    temp.append(li[m - 1][i])

                m -= 1

            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    temp.append(li[i][l])

                l += 1
#         top,left = 0,0
#         temp = []
#         bottom,right = len(matrix),len(matrix[0])
#         if bottom == 1:
#             return matrix[0]
#         if right == 1:
#             for i in matrix:
#                 temp.append(i[0])
#             return temp
            
#         while (top < bottom and left < right) :

#             for i in range(left,right):
#                 temp.append(matrix[top][i])
#             top += 1

#             for i in range(top,bottom):
#                 temp.append(matrix[i][right-1])
#             right -= 1

#             if right > left :
#                 for i in range(right-1,left-1,-1):
#                     temp.append(matrix[bottom-1][i])
#                 bottom -= 1

#             if bottom > top  :
#                 for i in range(bottom-1,top-1,-1):
#                     temp.append(matrix[i][left])
#                 left += 1
                
#         elif bottom > right:
#             while top < bottom and left < right :
                
#                 for i in range(left,right):
#                     temp.append(matrix[top][i])
#                 top += 1
                
#                 for i in range(top,bottom):
#                     temp.append(matrix[i][right-1])
#                 right -= 1
                
#                 if right > left :
#                     for i in range(right-1,left-1,-1):
#                         temp.append(matrix[bottom-1][i])
#                     bottom -= 1
                
#                 if bottom > top  + 1  :
#                     for i in range(bottom-1,top-1,-1):
#                         temp.append(matrix[i][left])
#                     left += 1
                
#         else:
#             while top < bottom and left < right :
                
#                 for i in range(left,right):
#                     temp.append(matrix[top][i])
#                 top += 1
                
#                 for i in range(top,bottom):
#                     temp.append(matrix[i][right-1])
#                 right -= 1
                
#                 if right > left + 1:
#                     for i in range(right-1,left-1,-1):
#                         temp.append(matrix[bottom-1][i])
#                     bottom -= 1

#                 if bottom > top   :
#                     for i in range(bottom-1,top-1,-1):
#                         temp.append(matrix[i][left])
#                     left += 1
        
        return temp