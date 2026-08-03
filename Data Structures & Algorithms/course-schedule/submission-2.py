class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph - indegree[i] = how many prereqs
        indegree = [0] * numCourses
        # adj[i] = list of courses that become "unlocked" (partially) once i is done
        adj = [[] for _ in range(numCourses)]

        # prereqs are given as [dst, src] pairs
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        # process courses in topo order
        finish = 0

        while q:
            node = q.popleft()
            finish += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # step 4 check result
        return finish == numCourses