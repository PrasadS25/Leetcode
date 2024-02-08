class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def ispalindrome(p):
            return p == p[::-1]
        def dfs(i):
            if i>=len(s):
                res.append(sub[::])
                return
            
            for j in range(i,len(s)):
                if ispalindrome(s[i:j+1]):
                    sub.append(s[i:j+1])
                    dfs(j+1)
                    sub.pop()
        dfs(0)
        return res