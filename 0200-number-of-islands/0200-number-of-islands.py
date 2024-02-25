class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        totalrows, totalcols = len(grid) , len(grid[0])
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r = row+dr
                    c = col+dc
                    if (r in range(totalrows)) and (c in range(totalcols)) and (grid[r][c] == "1") and ((r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
                
        for r in range(totalrows):
            for c in range(totalcols):
                if grid[r][c] ==  "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
                
        return islands