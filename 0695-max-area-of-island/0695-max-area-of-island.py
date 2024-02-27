class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs
        maxarea = 0
        totalrows, totalcols = len(grid), len(grid[0])

        def dfs(r,c):
            if r not in range(totalrows) or c not in range(totalcols) or grid[r][c] == 0:
                return 0
            area = 1
            grid[r][c] = 0
            for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                area += dfs(r+dr,c+dc)
            return area

        for r in range(totalrows):
            for c in range(totalcols):
                if grid[r][c] == 1:
                    maxarea = max(dfs(r,c),maxarea)
        return maxarea