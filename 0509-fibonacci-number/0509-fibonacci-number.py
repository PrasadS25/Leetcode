class Solution:
    def fib(self, n: int) -> int:
        
        dp = {}
        dp[0] = 0
        dp[1] = 1

        def rec(n):
            if n<= 1:
                return dp[n]
            if n in dp:
                return dp[n]
            dp[n] = rec(n-1) + rec(n-2)
            return dp[n]
        
        return rec(n)