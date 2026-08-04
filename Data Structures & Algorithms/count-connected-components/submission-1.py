class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def bfs(q):
            while q:
                popped = q.pop()
                for n in adj[popped]:
                    if visited[n] == False:
                        q.appendleft(n)
                        visited[n] = True

        count = 0

        for i in range(n):
            if not visited[i]:
                q = deque()
                q.append(i)
                bfs(q)
                count += 1

        return count
                    