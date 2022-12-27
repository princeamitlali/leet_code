class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev = 0
        for i in brackets:
            if income > i[0]:
                tax += ((i[0]-prev) * i[1]) /100
                prev = i[0]
            else:
                
                tax += ((income-prev) * i[1]) /100
                return tax
        return tax
                
        