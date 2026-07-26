class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tally_d = {}
        for task in tasks:
            if task in tally_d:
                tally_d[task] = tally_d[task] - 1
            else:
                tally_d[task] = -1
        pq = [(val, c) for c, val in tally_d.items()]
        heapq.heapify(pq)
        tally = 0

        while pq:
            len_pq = len(pq)
            n_slots = min(n + 1, len_pq) # u dont need to pop the full lenght of the arr
            to_repush = [] 
            for i in range(n_slots):
                tally += 1
                val, c = heapq.heappop(pq)
                val += 1
                if val < 0:
                    to_repush.append((val, c)) # doesn't go back in at all
            
            for val, c in to_repush:
                heapq.heappush(pq, (val, c))

            if pq:
                tally += n + 1 - n_slots 

        return tally