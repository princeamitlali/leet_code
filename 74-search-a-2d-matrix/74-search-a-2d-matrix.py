class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)== 1 :
            for i in matrix[0]:
                if i == target:
                    return True
            return False
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                if matrix[i][0] == target:
                    return True
            return False
        top,right = 0,len(matrix[0]) - 1
        while top < len(matrix) and right > -1:
            val = matrix[top][right]
            if  val == target:
                return True
            if val < target:
                top += 1
            else:
                right -= 1
        return False
                
        