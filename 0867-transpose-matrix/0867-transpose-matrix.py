class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix =  list(zip(*matrix))
        return matrix
        