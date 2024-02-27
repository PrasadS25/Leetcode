class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        totalrows, totalcols = len(grid), len(grid[0])
        
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = 0
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            area = 1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if (nr in range(0,totalrows)) and (nc in range(0,totalcols)) and (grid[nr][nc] == 1):
                        area += 1
                        grid[nr][nc] = 0
                        q.append((nr,nc))
            return area

        for r in range(totalrows):
            for c in range(totalcols):
                if grid[r][c] == 1:
                    maxarea = max(bfs(r,c),maxarea)

        return maxarea