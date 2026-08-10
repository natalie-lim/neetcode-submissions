class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inbound = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for second, first in prerequisites:
            if first == second:
                return False
            inbound[second] += 1
            adj[first].append(second)
        
        q = deque()
        for course, incoming in enumerate(inbound):
            if incoming == 0:
                q.append(course)
            
        while q:
            course = q.pop()
            for neighbor in adj[course]:
                val = inbound[neighbor]
                val -= 1
                inbound[neighbor] = val
                if val == 0:
                    q.appendleft(neighbor)
            
        for i in inbound:
            if i > 0:
                return False
        return True
                