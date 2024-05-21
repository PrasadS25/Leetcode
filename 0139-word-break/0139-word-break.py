class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def rec(target,words,dp={}):
            if target in dp:
                return dp[target]
            if target == "":
                return True
            
            for word in words:
                if target.find(word) == 0:
                    if rec(target[len(word):],words,dp):
                        dp[target] = True
                        return True
            dp[target] = False
            return False

        return rec(s,wordDict)