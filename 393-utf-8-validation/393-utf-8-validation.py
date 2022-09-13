class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        pt, num = 0, len(data)
        while pt < num:
            if data[pt] < 128:
                pt += 1
            elif 192 <= data[pt] < 224:
                if pt+2>num or not all(128<=data[i]<192 for i in range(pt+1,pt+2)):
                    return False
                pt += 2
            elif 224 <= data[pt] < 240:
                if pt+3>num or not all(128<=data[i]<192 for i in range(pt+1,pt+3)):
                    return False
                pt += 3
            elif 240 <= data[pt] < 248:
                if pt+4>num or not all(128<=data[i]<192 for i in range(pt+1,pt+4)):
                    return False
                pt += 4
            else:
                return False
        return True
        