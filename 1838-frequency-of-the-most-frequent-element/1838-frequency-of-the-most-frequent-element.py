class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        maxf = 0
        total = 0
        for j in range(len(nums)):
            total += nums[j]
            while i<j and nums[j]*(j-i+1) > total+k:
                total -= nums[i]
                i+=1
            maxf = max(maxf,j-i+1)
        return maxf