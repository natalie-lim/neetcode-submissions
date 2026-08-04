class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        visited = []
        adj = [[] for _ in range(n)]

        for c1, c2 in edges:
            adj[c1].append(c2)
            adj[c2].append(c1)
        

        def explore(n):
            if n in visited:
                return False
            neighbors = adj[n]
            adj[n] = []
            for neighbor in neighbors:
                explore(neighbor)
            for l in adj:
                if len(l) > 0:
                    return False
            return True

        return explore(0)