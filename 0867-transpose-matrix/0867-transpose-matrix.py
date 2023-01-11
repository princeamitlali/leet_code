class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix =  [list(i) for i in zip(*matrix)]
        return matrix
        