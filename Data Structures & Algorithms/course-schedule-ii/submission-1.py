class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        # if topo sort exists, let's use kahn's yay
        indegree = [0] * numCourses
        graph = defaultdict(list) 

        for course, pre in prerequisites:
            prev = indegree[course]
            indegree[course] = prev + 1

            graph[pre].append(course)
        
        sources = []
        for i, val in enumerate(indegree):
            if val == 0:
                sources.append(i)

        while len(sources) > 0:
            pop = sources.pop()
            res.append(pop)
            tos = graph[pop]
            for node in tos:
                prev = indegree[node]
                prev -= 1
                indegree[node] = prev
                if prev == 0:
                    sources.append(node)
        
        return res if len(res) == numCourses else []


