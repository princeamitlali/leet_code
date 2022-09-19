class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        temp = {}
        for i in paths:
            path, *file = i.split(" ")
            for j in file:
                f,d = j.split("(")
                # print(f,d)
                if d in temp:
                    val = temp[d]
                    # print(val)
                    val.append(path + "/" + f)
                    temp[d] = val
                else:
                    val = [path + "/" + f]
                    temp[d] = val
        result = []
        for i in temp:
            if len(temp[i]) > 1:
                result.append(temp[i])
        return result
            
                
    
        