class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxwater = 0
        while i<j:
            water = min(height[i],height[j]) * (j-i)
            maxwater = max(maxwater,water)
            if (height[i]<height[j]):
                i+=1
            else:
                j-=1

        return maxwater