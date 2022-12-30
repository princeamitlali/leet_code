class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        print(start)
        print(goal)
        ls = len(start)
        le = len(goal)
        if ls > le:
            goal = '0' * (ls-le) + goal
        else:
            start = '0' * (le-ls) + start
        c = 0
        for i in range(len(goal)):
            if start[i] != goal[i]:
                c += 1
            
        
        return c
        