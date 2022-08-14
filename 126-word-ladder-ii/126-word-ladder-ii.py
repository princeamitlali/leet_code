from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        prefix_d = defaultdict(list)
        for word in wordList:
            for i in range(0,len(word)):
                prefix_d[word[0:i]+"*"+word[i+1:]].append(word)
        
        order = {beginWord: []}
        queue = deque([beginWord])
        temp_q = deque()
        go_on = True
        end_list = []
        
        while queue and go_on:  # There is no node even added to temp_q
            temp_d = {}
            while queue:        # Pop every node on this level
                cur = queue.popleft()
                for i in range(0, len(cur)):
                    for j in prefix_d[cur[0:i]+"*"+cur[i+1:]]:
                        if j == endWord:
                            end_list.append(j)
                            go_on = False
                        if j not in order:
                            if j not in temp_d:
                                temp_d[j] = [cur]
                                temp_q.append(j)
                            else:
                                temp_d[j].append(cur)
            queue = temp_q
            temp_q = deque()
            order.update(temp_d)
        
        ret = []
        
        # DFS to restore the paths
        def dfs(path, node):
            path = path + [node]    # add the node(Deepcopy)
            if order[node] == []:
                ret.append(list(path[::-1]))
                return
            for i in order[node]:
                dfs(path, i)
        if endWord in order:
            dfs([], endWord)
        else:
            return []
        
        return ret