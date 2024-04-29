class Solution(object):
    def maxProfit(self, prices):
        p =0
        maxp =0
        l=0
        r=1
        while r<len(prices):

            if prices[l]<prices[r]:
                p = prices[r]-prices[l]
                maxp = max(maxp,p)
            else:
                l=r
            r+=1
        
        return maxp