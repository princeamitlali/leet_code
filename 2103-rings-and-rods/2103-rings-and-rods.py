class Solution:
    def countPoints(self, rings: str) -> int:
        rods = ["","","","","","","","","",""]
        c = 0
        for i in range(0,len(rings),2):
            rods[int(rings[i+1])] += rings[i]
        print(rods)
        for i in rods:
            if i == "":
                continue
            if "R" in i and "G" in i and "B" in i:
                c += 1
        return c
                
        