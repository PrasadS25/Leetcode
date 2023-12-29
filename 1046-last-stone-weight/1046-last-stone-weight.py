class Solution:
    def lastStoneWeight(self, stones) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            y= heapq.heappop(heap)
            x = heapq.heappop(heap)

            if x>y:
                heapq.heappush(heap,y-x)
            
        if len(heap)==1:
            return abs(heap[0])
        return 0
