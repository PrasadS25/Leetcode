class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        sub = []
        if len(digits)==0:
            return []
        maps = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        def dfs(i):
            if i>=len(digits):
                res.append(sub[:])
                return 

            for k in range(len(maps[digits[i]])):
                sub.append(maps[digits[i]][k])
                dfs(i+1)
                sub.pop()

        dfs(0)
        res = ["".join(pair) for pair in res]
        return res