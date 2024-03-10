class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # visit = set()
        # edges.sort()
        # for i in range(len(edges)):
        #     visit = set()
        #     visit.add(edges[i][0])
        #     visit.add(edges[i][1])
            
        #     for k in range(i+1,len(edges)):
        #         a,b = edges[k]
        #         if a in visit and b in visit:
        #             return edges[k]
        #         elif a in visit:
        #             visit.add(b)
        #         elif b in visit:
        #             visit.add(a)

        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            p = parent[n]

            while(p!= parent[p]):
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]