class Solution(object):
    def maxProfit(self, prices):
        p,maxp =0,0
        l,r=0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                maxp = max(maxp,prices[r]-prices[l])
            else:
                l=r
            r+=1
        
        return maxp