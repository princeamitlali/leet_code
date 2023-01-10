class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r=len(mat)
        c=len(mat[0])
        for i in range(r):
            for j in range(c):
                if mat[i][j]!=0:
                    top=mat[i-1][j] if i>0 else float('inf')
                    left=mat[i][j-1] if j>0 else float('inf')
                    mat[i][j]=min(top,left)+1
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if mat[i][j]!=0:
                    down=mat[i+1][j] if i<r-1 else float('inf')
                    right=mat[i][j+1] if j<c-1 else float('inf')
                    mat[i][j]=min(mat[i][j],min(down,right)+1)
        return mat
                          
                
            
        