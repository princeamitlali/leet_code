class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        temp = []
        for i in image:
            t = []
            for j in i[::-1]:
                if j == 0:
                    t.append(1)
                else:
                    t.append(0)
            temp.append(t)
        return temp
        