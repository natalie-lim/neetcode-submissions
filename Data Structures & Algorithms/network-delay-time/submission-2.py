class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)] # ui: (vi, ti)

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        heap = [] # min heap 
        heapq.heappush(heap, (0, k)) # dist, node
        visit = set()
        total_time = 0

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            total_time = dist
            neighbors = graph[node]
            new_neighbors = []
            while neighbors:
                vi, ti = neighbors.pop()
                if vi not in visit:
                    new_neighbors.append(((ti+dist), vi))
            graph[node] = new_neighbors
            heap = heap + new_neighbors
            heapq.heapify(heap)

        return total_time if len(visit) == n else -1
