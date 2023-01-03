class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dis = []
        not_dis = []
        for i in arr:
            if i in dis:
                dis.pop(dis.index(i))
                if i not in not_dis:
                    not_dis.append(i)
            else:
                if i not in not_dis:
                    dis.append(i)
        print(dis,not_dis)
        if k <= len(dis):
            return dis[k-1]
        return ""
        