class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        d = {}
        for i,c in enumerate(words):
            d[c] = i
        if "" in d:                       #  If sapces and pallindrome are present like as in example 3.
            j = d[""]
            for i in range(len(words)):
                if i != j and words[i] == words[i][::-1]:
                    ans.append([i,j])
                    ans.append([j,i])
                    
        for i in range(len(words)):        # Case for abcd and dcba like strings
            s = words[i][::-1]
            if s in d and d[s] != i:
                ans.append([i,d[s]])
                
        for i in range(len(words)):        # General Case for all other strings.
            for j in range(1,len(words[i])):
                l = words[i][0:j]
                r = words[i][j:]
                if l == l[::-1]:
                    if r[::-1] in d and d[r[::-1]] != i:
                        ans.append([d[r[::-1]],i])
                if r == r[::-1]:
                    if l[::-1] in d and d[l[::-1]] != i:
                        ans.append([i,d[l[::-1]]])
        return ans
#         ans =[]
#         dic = {}
        
#         for i,word in enumerate(words):
#             dic[word] = i
            
#         if "" in dic or " " in dic:
#             j = dic[""]
#             for i in range(len(words)):
#                 if i != j and words[i] == words[i][::-1]:
#                     ans.append([i,j])
#                     ans.append([j,i])
#         for i in range(len(words)):
#             s = words[i][::-1]
#             if s in dic and dic[s] !=1:
#                 ans.append([i,dic[s]])
#         for i in range(len(words)):        # General Case for all other strings.
#             for j in range(1,len(words[i])):
#                 l = words[i][0:j]
#                 r = words[i][j:]
#                 if l == l[::-1]:
#                     if r[::-1] in dic and dic[r[::-1]] != i:
#                         ans.append([dic[r[::-1]],i])
#                 if r == r[::-1]:
#                     if l[::-1] in dic and dic[l[::-1]] != i:
#                         ans.append([i,dic[l[::-1]]])
#         return ans
        