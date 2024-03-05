class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        time = 0
        rotten = collections.deque()
        rows,cols = len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r,c])
                elif grid[r][c] == 1:
                    fresh +=1

        while rotten and fresh>0:

            for i in range(len(rotten)):
                r,c = rotten.popleft()
                for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                    row,col = r+dr,c+dc
                    if row<0 or col<0 or row==rows or col==cols or grid[row][col]!=1:
                        continue
                    grid[row][col] = 2
                    fresh -=1
                    rotten.append([row,col])
            time +=1

        
        return time if fresh==0 else  -1