class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*(len(arr)+1)

        for i in range(1,len(arr)+1):
            maxv = 0 
            for j in range(1,min(k,i)+1):
                maxv = max(maxv,arr[i-j])
                dp[i] = max(dp[i],maxv*j+dp[i-j])

        return dp[len(arr)]