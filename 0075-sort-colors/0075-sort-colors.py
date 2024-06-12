class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maps = {0:0,1:0,2:0}
        for i in nums:
            maps[i] +=1
           
        for i in range(len(nums)):
            if maps[0]>0:
                nums[i] = 0
                maps[0]-=1
            elif maps[1]>0:
                nums[i] = 1
                maps[1]-=1
            else:
                nums[i] = 2
                maps[2]-=1