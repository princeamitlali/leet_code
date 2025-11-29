class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        sol = []
        for i in order:
            if i in friends:
                sol.append(i)
        return sol
        