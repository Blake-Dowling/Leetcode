class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Right edge
        r = len(grid) - 2
        c = len(grid[r]) - 1
        while r >= 0:
            grid[r][c] = grid[r][c] + grid[r+1][c]
            r -= 1
        #Bottom edge
        r = len(grid) - 1
        c = len(grid[r]) - 2
        while c >= 0:
            grid[r][c] = grid[r][c] + grid[r][c+1]
            c -= 1
        #Second-from-right column, with diagonals
        r = len(grid) - 2
        c = len(grid[r]) - 2
        while r >= 0:
            i = 0
            while c - i >= 0 and r + i <= len(grid) - 2:
                grid[r+i][c-i] = min(grid[r+i][c-i] + grid[r+i][c-i+1], grid[r+i][c-i] + grid[r+i+1][c-i])
                i += 1
            r -= 1
        #Remaining top
        r = 0
        c = len(grid[r]) - 3
        while c >= 0:
            i = 0
            while c - i >= 0 and r + i <= len(grid) - 2:
                grid[r+i][c-i] = min(grid[r+i][c-i] + grid[r+i][c-i+1], grid[r+i][c-i] + grid[r+i+1][c-i])
                i += 1
            c -= 1
        return grid[0][0]


