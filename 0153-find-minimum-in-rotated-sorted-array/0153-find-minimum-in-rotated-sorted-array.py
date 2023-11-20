class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        if nums[l] <= nums[r]:
            return nums[0]
        while nums[l]>nums[r]:
                mid = (l+r)//2
                if nums[mid] > nums[r]:
                    l = mid+1
                elif nums[mid] <= nums[r]:
                    r = mid
        if nums[l]<=nums[r]:
            return nums[l]