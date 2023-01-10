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
                          
                
            
        print("here")
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    mat[i][j] = 99999999999999
        for i in range(n):
            for j in range(m):
                l=r=u=p = 999999999999999
                # print(mat[i][j])
                if mat[i][j] != 0:
                    # if -1 < i-1 :
                    #     l = mat[i-1][j]
                    #     if l == 0:
                    #         mat[i][j] = 1
                    #         continue
                    if i+1 < n :
                        r = mat[i+1][j]
                        if r == 0:
                            mat[i][j] = 1
                            continue
                    # if -1 < j-1 :
                    #     u = mat[i][j-1]
                    #     if u == 0:
                    #         mat[i][j] = 1
                    #         continue
                    if j+1 < m :
                        p = mat[i][j+1]
                        if p == 0:
                            mat[i][j] = 1
                            continue
                    
                    # print(l,r,u,p,min(l,r,u,p))
                    mat[i][j] = min(l,r,u,p) + 1
                    
        return mat
        