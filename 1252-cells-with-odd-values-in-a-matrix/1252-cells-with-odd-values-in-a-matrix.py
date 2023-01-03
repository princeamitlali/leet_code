class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        val = [[0 ]* n for i in range(m)]
        print(val)
        for (i,j) in indices:
            
            val[i]=list(map(lambda x: x+1,val[i]))
            for k in range(m):
                
                val[k][j] +=  1 
        res = 0
        for i in val:
            for j in i:
                if j %2 == 1:
                    res += 1
        
        return res