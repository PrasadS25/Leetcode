class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # maps = {}
        for i in board:
            maps = {}
            for j in i:
                
                if j=='.':
                    continue
                if maps.get(j):
                    return False
                maps[j] = 1

        i=0
        j=0
        for n in range(0,9):
            maps={}
            for m in range(0,9):
                
                num = board[m][n]
                if num == '.':
                    continue
                if maps.get(num):
                    return False
                maps[num] = 1
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                maps={}
                for m in range(i,i+3):
                    for n in range(j,j+3):
                        num = board[m][n]
                        if num=='.':
                            continue
                        if maps.get(num):
                            return False
                        maps[num]=1
        return True