class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        temp2 = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in temp:
                        temp.append(i)
                    if j not in temp2:
                        temp2.append(j)
        print(temp,temp2)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in temp or j in temp2:
                    matrix[i][j] = 0