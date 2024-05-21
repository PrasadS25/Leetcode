class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))

        for i in range(len(nums)-1,-1,-1):
            maxv = 1
            for j in range(i,len(nums)):
                if nums[j]>nums[i]:
                    maxv = max(maxv,dp[j]+1)
            dp[i] = maxv

        return max(dp)