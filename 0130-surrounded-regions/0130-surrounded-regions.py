class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows,cols = len(board),len(board[0])
        unflip = set()

        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                dfs(r+dr,c+dc)

        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'