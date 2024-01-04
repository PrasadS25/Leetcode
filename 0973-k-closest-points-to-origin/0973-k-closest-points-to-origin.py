class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []
        for (x,y) in points:
            val = -(x*x + y*y)
            heapq.heappush(heap,(val,x,y))
            if len(heap)>k:
                heapq.heappop(heap)
        for (val,x,y) in heap:
            res.append([x,y])

        return res