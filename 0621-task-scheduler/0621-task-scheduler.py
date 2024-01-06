class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maps = {}
        for task in tasks:
            maps[task] = 1 + maps.get(task,0)
        
        vals = [-x for x in maps.values()]

        heapq.heapify(vals)
        queue = collections.deque()
        time = 0
        while len(queue) or len(vals):
            time += 1
            if len(vals):
                k = heapq.heappop(vals)
                k += 1
                if k != 0:
                    queue.append([k,time+n])
            if len(queue) and queue[0][1] == time :
                k = queue.popleft()
                heapq.heappush(vals,k[0])  
        return time