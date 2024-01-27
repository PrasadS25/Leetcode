class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        heapq.heapify(self.small)
        heapq.heapify(self.big)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1 * num)

        if self.small and self.big:
            if (-1*self.small[0]) > self.big[0]:
                a =heapq.heappop(self.small) * -1
                heapq.heappush(self.big,a)

        if abs(len(self.small) - len(self.big)) > 1:
            if len(self.small) > len(self.big):
                a = heapq.heappop(self.small)* -1
                heapq.heappush(self.big,a)
            else:
                a = heapq.heappop(self.big)
                heapq.heappush(self.small,-1 * a)
                
    def findMedian(self) -> float:
        
        if len(self.small) == len(self.big):
            return ((self.small[0]* -1)+self.big[0])/2
        elif len(self.small) > len(self.big):
            return (self.small[0])* -1
        else:
            return self.big[0]