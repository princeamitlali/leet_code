class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = []
        for i in logs:
            if i == "../":
                if len(res)>0:
                    res.pop()
            elif i != "./":
                res.append(i)
            # print(res)
        return len(res)
        