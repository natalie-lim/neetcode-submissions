class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {} #task, freq

        for task in tasks:
            if task in d:
                val = d[task]
                d[task] = val + 1
            else:
                d[task] = 1
        
        # heap based on -freq
        heap = []

        for task, freq in d.items():
            heapq.heappush(heap, (-freq, task))
        
        total = 0
        cycle_len = n + 1

        while heap:
            to_append = []
            used = 0
            for i in range(cycle_len):
                if heap:
                    freq, task = heapq.heappop(heap)
                    freq += 1
                    used += 1
                    if freq < 0:
                        to_append.append((freq, task))
            if heap or to_append:
                total += cycle_len
            else:
                total += used
            heap = to_append + heap
            heapq.heapify(heap)

        return total