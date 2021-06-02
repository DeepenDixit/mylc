class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island_number = 2
        
        def check(grid, i, j, r, c):
            if i < 0 or j < 0 or i > r-1 or j > c-1:
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = island_number
                
                check(grid, i, j+1, r, c)
                check(grid, i-1, j, r, c)
                check(grid, i, j-1, r, c)
                check(grid, i+1, j, r, c)
        
        row = len(grid)
        column = len(grid[0])
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    check(grid, i, j, row, column)
                    island_number += 1
        
        flatten = list()
        for i in grid:
            flatten.extend(i)
        
        result = 0
        for i in range(2,island_number):
            j = flatten.count(i)
            if j >= result:
                result = j
        
        return result