class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # dic = {}
        # for i in edges:
        #     key,val = i[0],i[1]
        #     if key in dic.keys():
        #         v = dic[key]
        #         v.append(val)
        #         dic[key] = v
        #     else:
        #         dic[key] = [val]
        # # print(dic)
        # for i in dic:
        #     key,val = i,dic[i]
        #     temp = []
        #     for j in val:
        #         if j in dic.keys():
        #             for k in dic[j]:
        #                 val.append(k)
        #         # print(j,val)
        #     # temp.append(val)
        #     dic[key] = list(set(val))
        # print(dic)
        # res = [1 for i in range(n)]
        # for i in dic:
        #     key,val = i,dic[i]
        #     r = 1
        #     for j in val:
        #         if labels[key] == labels[j]:
        #             r += 1
        #     res[i] = r
        # return res
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = [0] * n

        def dfs(vertex: int, parent: int, cnt: collections.Counter) -> None:
            before = cnt[labels[vertex]]

            for adjacent in graph[vertex]:
                if adjacent != parent:
                    dfs(adjacent, vertex, cnt)

            cnt[labels[vertex]] += 1
            ans[vertex] = cnt[labels[vertex]] - before

        dfs(0, 0, collections.Counter())
        return ans  