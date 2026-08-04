class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        visited = [0] * n

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(n):
            if visited[n] == 1:
                return
            visited[n] = 1
            for neighbor in adj[n]:
                dfs(neighbor)

        ccs = 0

        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                ccs += 1
        
        return ccs