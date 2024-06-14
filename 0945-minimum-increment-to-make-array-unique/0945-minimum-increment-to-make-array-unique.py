class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(1,len(nums)):
            diff = nums[i-1] - nums[i]
            if diff>=0:
                count+=diff+1
                nums[i] += diff+1
        return count