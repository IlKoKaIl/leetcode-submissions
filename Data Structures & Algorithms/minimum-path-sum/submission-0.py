class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):

                if r == 0 and c == 0:
                    continue
                
                top = float('inf')
                left = float('inf')

                if r > 0:
                    top = grid[r-1][c]
                
                if c > 0 :
                    left = grid[r][c-1]
                
                grid[r][c] += min(top, left)
            
        return grid[-1][-1]
        