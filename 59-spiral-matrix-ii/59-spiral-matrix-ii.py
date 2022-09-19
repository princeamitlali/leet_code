class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        val = n* n + 1
        li = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
        m = n
        k = 0
        l = 0
        temp = []
        j = 1
        while j < val:
            for i in range(l, n):
                li[k][i] = j
                j += 1

            k += 1
            
            for i in range(k, m):
                li[i][n - 1] = j
                j += 1

            n -= 1
            
            if (k < m):

                for i in range(n - 1, (l - 1), -1):
                    li[m - 1][i] = j
                    j += 1

                m -= 1
            

            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    li[i][l] = j
                    j += 1

                l += 1 
            
        return li
        