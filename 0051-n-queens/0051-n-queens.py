class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posi = set()
        neg = set()
        board = [["."]*n for i in range(n)]
        res = []

        def backtrack(r):

            if r==n:
                new = ["".join(row) for row in board]
                res.append(new)
                return 
            
            for c in range(n):
                if c in cols or (r+c) in posi or (r-c) in neg:
                    continue
                #add the current cell to columns, positive diagnoal and negative diagnoal.
                cols.add(c)
                posi.add(r+c)
                neg.add(r-c)
                board[r][c] = 'Q'
                
                backtrack(r+1)

                cols.remove(c)
                posi.remove(r+c)
                neg.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return res