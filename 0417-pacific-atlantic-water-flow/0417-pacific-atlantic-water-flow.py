class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific = set()
        atlantic = set()
        totalrows, totalcols = len(heights),len(heights[0])

        def dfs(r,c,visit,prevH):
            if ((r,c) in visit or r<0 or c<0 or r==totalrows or c==totalcols or
                heights[r][c]<prevH):
                return
            visit.add((r,c))
            for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                dfs(r+dr,c+dc,visit,heights[r][c])

        for c in range(totalcols):
            dfs(0,c,pacific,0)
            dfs(totalrows-1,c,atlantic,0)
        for r in range(totalrows):
            dfs(r,0,pacific,0)
            dfs(r,totalcols-1,atlantic,0)

        for r in range(totalrows):
            for c in range(totalcols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res