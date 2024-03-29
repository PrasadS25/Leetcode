class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board),len(board[0])
        path = set()
        def dfs(r,c,i):

            if i==len(word):
                return True
            if (r>=rows or c>=cols or
                r<0 or c<0 or (r,c) in path
                or word[i]!= board[r][c]):
                return False

            path.add((r,c))
            res = (dfs(r,c+1,i+1) or
                    dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c-1,i+1))
            path.remove((r,c))
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0): return True
        return False 
