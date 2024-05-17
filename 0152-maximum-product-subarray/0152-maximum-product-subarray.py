class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin,curMax = 1,1
        maxv = max(nums)
        
        for num in nums:
            k = num*curMax
            curMax = max(k,num*curMin,num) 
            curMin = min(k,num*curMin,num) 

            maxv = max(curMax,maxv)

        return maxv