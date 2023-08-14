class Solution:
    def slidingPuzzle(self, grid: List[List[int]]) -> int:
        def is_valid(x,y):
            return -1 <x <2 and -1<y<3
        
        def is_solution(grid):
            return grid == [[1,2,3],[4,5,0]]
        
        def index_of_blank(grid):
            for i in range(2):
                for j in range(3):
                    if grid[i][j] == 0:
                        return i,j
        def swap(grid,x1,y1,x2,y2):
            grid[x1][y1],grid[x2][y2] = grid[x2][y2],grid[x1][y1]
            
        def get_neighbors(grid):
            neighbors = []
            r, c = 0, 0
            r,c = index_of_blank(grid)
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + i, c + j
                if is_valid(new_r,new_c) :
                    new_grid = [row[:] for row in grid]
                    swap(new_grid,r,c,new_r,new_c)
                    neighbors.append(new_grid)
            return neighbors
        def grid_to_tuple(grid):
            return tuple(tuple(row) for row in grid)
        
        queue = []
        queue.append((grid, 0)) # adding to queue from behind
        seen = set()
        seen.add(grid_to_tuple(grid))
        while queue:

            grid, moves = queue.pop(0) #leaving from front
            # print(grid)
            if is_solution(grid):
                return moves
            for neighbor in get_neighbors(grid):
                if  grid_to_tuple(neighbor) not in seen:
                    queue.append((neighbor, moves + 1))
                    seen.add(grid_to_tuple(neighbor))
        return -1
            
        