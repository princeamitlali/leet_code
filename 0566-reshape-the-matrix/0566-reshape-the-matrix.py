class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        linear_list = []
        for i in mat:
            for j in i:
                linear_list.append(j)
        if r*c!=len(linear_list):
            return mat
        mat_new = []
        for i in range(0,len(linear_list),c):
            mat_new.append(linear_list[i:i+c])
        return mat_new
