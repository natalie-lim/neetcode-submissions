class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)
        
        q = deque()
        for course, count in enumerate(indegree):
            if count == 0:
                q.append(course)

        topo = []
        # q only contains sources
        while q:
            popped = q.pop()
            topo.append(popped)
            for node in adj[popped]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        
        if len(topo) == numCourses:
            return topo
        else:
            return []