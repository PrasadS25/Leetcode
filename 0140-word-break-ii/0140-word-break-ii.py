class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def rec(target,words,dp={}):
            if target in dp:
                return dp[target]
            if target == "":
                return [[]]
            res = []
            for word in words:
                if target.find(word) == 0:
                    other = rec(target[len(word):],words,dp)
                    final = [[word] + x for x in other]
                    res.extend(final)
            dp[target] = res
            return res
        res = rec(s,wordDict)
        result = []
        for i in res:
            result.append(" ".join(i))
        return result