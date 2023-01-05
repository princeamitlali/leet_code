class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        li = [i+1 for i in range(m)]
        # print(li)
        res = []
        for i in queries:
            v = li.index(i)
            res.append(v)
            li.pop(v)
            li.insert(0,i)
            # print(res,li)
        return res
            
        