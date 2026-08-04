class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]

        for c1, c2 in edges:
            adj[c1].append(c2)
            adj[c2].append(c1)

        visited = set()
        

        def explore(n):
            visited.add(n)
            for neighbor in adj[n]:
                if neighbor not in visited:
                    explore(neighbor)
        
        explore(0)
        return len(visited) == n