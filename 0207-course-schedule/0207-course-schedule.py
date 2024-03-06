class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        maps = {i:[] for i in range(numCourses)}

        visit = set()
        for crs, pre in prerequisites:
            maps[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if maps[crs] == []:
                return True
            
            visit.add(crs)
            for pre in maps[crs]:
                if not dfs(pre): return False
            maps[crs] = []
            visit.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True