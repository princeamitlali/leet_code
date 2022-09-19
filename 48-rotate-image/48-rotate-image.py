class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(m):
            for i in range(len(m)):
                for j in range(i+1,len(m[0])):
                    m[i][j],m[j][i] = m[j][i],m[i][j]
            return m
        
        matrix = transpose(matrix)
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]