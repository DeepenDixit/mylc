class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        cache = {}
        
        def check(r, c):
            if r>=row or c>=col:
                return 0
            
            if (r,c) not in cache:
                down = check(r+1, c)
                right = check(r, c+1)
                diagonal = check(r+1, c+1)
                
                cache[(r,c)] = 0
                if matrix[r][c] == '1':
                    cache[(r,c)] = min(down, right, diagonal) + 1
                
            return cache[(r,c)]
            
        check(0,0)
        return max(cache.values())**2
            

########################################################################