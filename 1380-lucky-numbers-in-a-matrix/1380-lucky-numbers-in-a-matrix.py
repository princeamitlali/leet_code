class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        trans = [list(i) for i in zip(*matrix)]
        res = []
        for i in range(len(matrix)):
            v = min(matrix[i])
            for j in range(len(matrix[0])):
                matrix[i][j] = v
        for i in range(len(trans)):
            v = max(trans[i])
            for j in range(len(trans[0])):
                trans[i][j] = v
        trans = [list(i) for i in zip(*trans)]
        print(trans,matrix)
        for i in range(len(trans)):
            for j in range(len(trans[0])):
                if trans[i][j] == matrix[i][j]:
                    res.append(trans[i][j])
                
        return res
        